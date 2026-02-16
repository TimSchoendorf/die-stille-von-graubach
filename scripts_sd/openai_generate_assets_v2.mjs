#!/usr/bin/env node
/**
 * Generate Visual Novel backgrounds + character portraits with OpenAI image model.
 * - No Stable Diffusion
 * - Consistent shared style across backgrounds + portraits
 * - Portraits use transparent background
 * - Writes new files as *_v2.png
 * - Optionally rewrites dialogue JSON references to *_v2
 *
 * Usage:
 *   node scripts_sd/openai_generate_assets_v2.mjs --rewrite-json
 *   OPENAI_API_KEY=... node scripts_sd/openai_generate_assets_v2.mjs --force --rewrite-json
 */

import fs from 'node:fs/promises';
import path from 'node:path';

const ROOT = process.cwd();
const DIALOGUE_DIR = path.join(ROOT, 'data', 'dialogue');
const BG_DIR = path.join(ROOT, 'assets', 'sprites', 'backgrounds');
const CHAR_DIR = path.join(ROOT, 'assets', 'sprites', 'characters');

const argv = process.argv.slice(2);
const FORCE = argv.includes('--force');
const REWRITE_JSON = argv.includes('--rewrite-json');
const DRY_RUN = argv.includes('--dry-run');
const MODEL = getArgValue('--model') || 'gpt-image-1';

const API_KEY = process.env.OPENAI_API_KEY || '';

const STYLE_BIBLE = [
  'Unified art direction for a 1920s German horror visual novel.',
  'Painterly realism, oil-on-canvas brushwork, muted desaturated palette, soft film grain.',
  'Cinematic chiaroscuro lighting, atmospheric fog, restrained contrast, no neon colors.',
  'Keep facial anatomy realistic and stable across variants.',
  'No anime/chibi/cartoon look.',
].join(' ');

const BACKGROUND_BRIEFS = {
  berlin_apartment: 'small 1920s Berlin apartment, books, desk, rain on window, cramped scholarly space',
  blacksmith_shop: '1920s blacksmith interior, forge embers, iron tools, worn wood and metal',
  church_basement: 'hidden stone chamber under church, carved symbols, damp walls, torchlight',
  church_corrupted: 'same village church but reality-distorted, warped pews, impossible shadows',
  church_exterior: 'old black forest village church exterior, fog, cemetery, overcast sky',
  church_interior: 'old church interior, pews, altar, dim stained glass light',
  forest_corrupted: 'black forest with surreal geometry and subtle cosmic corruption',
  forest_path: 'dense black forest path, pine trees, fog, late autumn',
  grandmother_house: 'interior of old german cottage, candlelit bedroom, herbal details',
  grandmother_house_night: 'same cottage interior at night, moonlit, unnerving shadows',
  hilde_cottage: 'herbalist cottage interior, jars, dried herbs, rustic textures',
  ritual_chamber: 'ancient underground ritual chamber, carved circle and altar, oppressive atmosphere',
  train_interior: '1920s European train compartment, wood and leather, journey mood',
  village_corrupted: 'same village square area but subtly corrupted by cosmic horror',
  village_entrance: 'entrance to black forest village, timber houses, heavy fog, silence',
  village_night: 'village streets at night, moonlight, deep fog, deserted',
  village_school: '1920s village classroom, wooden desks, chalkboard, empty room',
  village_square: 'village square with fountain, timber houses, church in distance',
};

const CHARACTER_IDENTITY = {
  anna: 'Anna, female, 19, pale blonde hair, very pale skin, light blue eyes, ethereal and fragile look, simple white dress',
  elise: 'Elise, female, 24, dark-brown bob hair, round glasses, brown eyes, slim build, serious intellectual demeanor, 1920s coat and blouse',
  georg: 'Georg, male, 45, broad blacksmith build, dark hair with gray, weathered skin, moustache, work clothes with leather apron',
  hilde: 'Hilde, female, 68, white braided hair, weathered wise face, green eyes, herbalist clothing in earth tones',
  konrad: 'Konrad, male, 30, handsome, wavy dark hair, warm brown eyes, teacher attire from the 1920s',
  otto: 'Otto, male, 60, heavyset, slicked-back gray hair, thick moustache, formal mayor suit, imposing presence',
  voss: 'Voss, male, 55, gaunt pastor, thin gray hair, hollow cheeks, dark tired eyes, black clerical robes with white collar',
};

const EXPRESSION_BRIEFS = {
  afraid: 'frightened, tense eyes, fear visible',
  angry: 'anger, furrowed brows, jaw set',
  authoritative: 'commanding, strict authority',
  broken: 'emotionally broken, exhausted despair',
  charming: 'warm charming smile, charismatic',
  dark: 'sinister undertone, shadowed expression',
  desperate: 'desperate, near panic, strained face',
  determined: 'resolute, focused, determined gaze',
  dreamy: 'distant dreamy gaze, detached',
  jovial: 'jovial, hearty expression',
  kind: 'gentle kindness, warm eyes',
  lucid: 'sudden clarity, alert urgency',
  mysterious: 'enigmatic half-smile, guarded eyes',
  neutral: 'neutral expression, calm',
  possessed: 'unnatural possession, unsettling eyes',
  praying: 'prayerful, hands clasped, solemn',
  protective: 'protective sternness, defensive posture',
  ritual: 'focused ritual concentration',
  sad: 'sadness, heavy eyes',
  smiling: 'soft sincere smile',
  suspicious: 'narrowed eyes, suspicion',
  thinking: 'thoughtful, contemplative',
  threatening: 'cold threat, intimidating look',
  warning: 'urgent warning expression',
  worried: 'anxious concern, slight frown',
};

function getArgValue(name) {
  const idx = argv.indexOf(name);
  if (idx >= 0 && idx + 1 < argv.length) return argv[idx + 1];
  return '';
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function listDialogueFiles(dir) {
  const out = [];
  async function walk(cur) {
    const entries = await fs.readdir(cur, { withFileTypes: true });
    for (const ent of entries) {
      const fp = path.join(cur, ent.name);
      if (ent.isDirectory()) await walk(fp);
      else if (ent.isFile() && ent.name.toLowerCase().endsWith('.json')) out.push(fp);
    }
  }
  await walk(dir);
  return out;
}

function collectUsage(dialogues) {
  const backgrounds = new Set();
  const characterExpressions = new Map();

  for (const doc of dialogues) {
    const nodes = doc?.nodes || {};
    for (const node of Object.values(nodes)) {
      if (node?.background) backgrounds.add(String(node.background));

      const setExpr = (charId, expr) => {
        if (!charId || !expr) return;
        if (!characterExpressions.has(charId)) characterExpressions.set(charId, new Set());
        characterExpressions.get(charId).add(expr);
      };

      if (node?.character && node?.expression) setExpr(String(node.character), String(node.expression));
      if (node?.speaker && node?.expression) setExpr(String(node.speaker), String(node.expression));
    }
  }

  return { backgrounds, characterExpressions };
}

async function readDialogues() {
  const files = await listDialogueFiles(DIALOGUE_DIR);
  const docs = [];
  for (const file of files) {
    const raw = await fs.readFile(file, 'utf8');
    const sanitized = raw.replace(/^\uFEFF/, '');
    docs.push({ file, json: JSON.parse(sanitized) });
  }
  return docs;
}

function makeBackgroundPrompt(name) {
  const brief = BACKGROUND_BRIEFS[name] || `${name}, black forest village horror setting`;
  return [
    STYLE_BIBLE,
    'Create a background-only scene with no people.',
    'Scene brief:',
    brief + '.',
    'Framing: widescreen visual novel background, environment storytelling details, depth and atmosphere.',
    'Safety: no text, no logos, no watermark.',
  ].join(' ');
}

function makePortraitPrompt(charId, expr) {
  const identity = CHARACTER_IDENTITY[charId] || `${charId}, human character in 1920s Germany`;
  const mood = EXPRESSION_BRIEFS[expr] || expr;
  return [
    STYLE_BIBLE,
    'Create a character portrait sprite for a visual novel.',
    'Transparent background only; do not paint any backdrop.',
    'Upper-body or half-body framing, centered, facing viewer.',
    'Keep identity stable and recognizable across emotional variants for the same character.',
    `Character identity: ${identity}.`,
    `Expression: ${mood}.`,
    'Safety: no text, no logos, no watermark.',
  ].join(' ');
}

async function callOpenAIImage({ prompt, size, transparent }) {
  if (DRY_RUN) return { dryRun: true, b64: null };

  const body = {
    model: MODEL,
    prompt,
    size,
    quality: 'high',
  };

  if (transparent) body.background = 'transparent';

  const res = await fetch('https://api.openai.com/v1/images/generations', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });

  const text = await res.text();
  let data = {};
  try { data = JSON.parse(text); } catch {}

  if (!res.ok) {
    const msg = data?.error?.message || text || `HTTP ${res.status}`;
    throw new Error(msg);
  }

  const b64 = data?.data?.[0]?.b64_json || data?.output?.[0]?.b64_json || null;
  const url = data?.data?.[0]?.url || data?.output?.[0]?.url || null;

  if (b64) return { b64 };
  if (url) {
    const imgRes = await fetch(url);
    if (!imgRes.ok) throw new Error(`Image URL fetch failed: ${imgRes.status}`);
    const arr = new Uint8Array(await imgRes.arrayBuffer());
    return { bytes: arr };
  }

  throw new Error('No image payload returned by API.');
}

async function writeImage(outPath, result) {
  await fs.mkdir(path.dirname(outPath), { recursive: true });

  if (result.dryRun) {
    console.log(`[dry-run] ${outPath}`);
    return;
  }

  if (result.b64) {
    const buf = Buffer.from(result.b64, 'base64');
    await fs.writeFile(outPath, buf);
    return;
  }

  if (result.bytes) {
    await fs.writeFile(outPath, Buffer.from(result.bytes));
    return;
  }

  throw new Error('Invalid image result payload');
}

async function generateBackgrounds(backgrounds) {
  const generated = new Set();
  for (const name of [...backgrounds].sort()) {
    const outPath = path.join(BG_DIR, `${name}_v2.png`);
    if (!FORCE) {
      try {
        await fs.access(outPath);
        console.log(`skip existing background: ${name}_v2`);
        generated.add(name);
        continue;
      } catch {}
    }

    const prompt = makeBackgroundPrompt(name);
    console.log(`generate background: ${name}_v2`);
    const result = await callOpenAIImage({ prompt, size: '1792x1024', transparent: false });
    await writeImage(outPath, result);
    generated.add(name);
    await sleep(400);
  }
  return generated;
}

async function generatePortraits(characterExpressions) {
  const generated = new Map();

  for (const charId of [...characterExpressions.keys()].sort()) {
    const expressions = [...characterExpressions.get(charId)].sort();
    for (const expr of expressions) {
      const outPath = path.join(CHAR_DIR, charId, `${expr}_v2.png`);

      if (!FORCE) {
        try {
          await fs.access(outPath);
          console.log(`skip existing portrait: ${charId}/${expr}_v2`);
          if (!generated.has(charId)) generated.set(charId, new Set());
          generated.get(charId).add(expr);
          continue;
        } catch {}
      }

      const prompt = makePortraitPrompt(charId, expr);
      console.log(`generate portrait: ${charId}/${expr}_v2`);
      const result = await callOpenAIImage({ prompt, size: '1024x1792', transparent: true });
      await writeImage(outPath, result);
      if (!generated.has(charId)) generated.set(charId, new Set());
      generated.get(charId).add(expr);
      await sleep(400);
    }
  }

  return generated;
}

async function rewriteDialogueReferences(dialogues, generatedBgs, generatedPortraits) {
  for (const entry of dialogues) {
    const doc = entry.json;
    const nodes = doc?.nodes || {};

    for (const node of Object.values(nodes)) {
      if (node?.background && generatedBgs.has(String(node.background)) && !String(node.background).endsWith('_v2')) {
        node.background = `${node.background}_v2`;
      }

      if (node?.character && node?.expression) {
        const charId = String(node.character);
        const expr = String(node.expression);
        if (generatedPortraits.has(charId) && generatedPortraits.get(charId).has(expr) && !expr.endsWith('_v2')) {
          node.expression = `${expr}_v2`;
        }
      }

      if (node?.speaker && node?.expression) {
        const charId = String(node.speaker);
        const expr = String(node.expression);
        if (generatedPortraits.has(charId) && generatedPortraits.get(charId).has(expr) && !expr.endsWith('_v2')) {
          node.expression = `${expr}_v2`;
        }
      }
    }

    const pretty = JSON.stringify(doc, null, '\t') + '\n';
    await fs.writeFile(entry.file, pretty, 'utf8');
  }
}

async function main() {
  if (!DRY_RUN && !API_KEY) {
    throw new Error('OPENAI_API_KEY is missing. Set it and rerun.');
  }

  const dialogues = await readDialogues();
  const usage = collectUsage(dialogues.map((d) => d.json));

  console.log(`backgrounds in use: ${usage.backgrounds.size}`);
  console.log(`characters in use: ${usage.characterExpressions.size}`);

  const generatedBgs = await generateBackgrounds(usage.backgrounds);
  const generatedPortraits = await generatePortraits(usage.characterExpressions);

  if (REWRITE_JSON && !DRY_RUN) {
    await rewriteDialogueReferences(dialogues, generatedBgs, generatedPortraits);
    console.log('dialogue references rewritten to *_v2 where generated.');
  } else if (REWRITE_JSON && DRY_RUN) {
    console.log('dry-run active: skipped dialogue rewrite.');
  } else {
    console.log('skipped dialogue rewrite (pass --rewrite-json to enable).');
  }

  console.log('done');
}

main().catch((err) => {
  console.error('error:', err.message);
  process.exit(1);
});
