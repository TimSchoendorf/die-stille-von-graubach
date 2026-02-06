"""
Charakter-Sprite Generierung V2 - img2img Ansatz
==================================================
Workflow pro Charakter:
1. Referenzbild (neutral) per txt2img generieren
2. Alle Expressions per img2img vom Referenzbild ableiten (Denoising 0.65)
   -> Koerper/Kleidung/Pose bleiben konsistent, nur Expression aendert sich

Settings:
- Modell: Animagine XL 3.1 (Oil Painting Stil)
- Aufloesung: 832x1216 (Portrait)
- Sampler: DPM++ 2M SDE Karras, 28 Steps, CFG 7
- Pose-Locking: front view, centered, symmetrical
- rembg: isnet-anime (0.3s, spezialisiert fuer Anime)
- Sprite: 600x900 mit konsistentem Cropping
- img2img Denoising: 0.65 (Standard)
"""
import argparse
import base64
import io
import json
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from PIL import Image

SD_URL = "http://127.0.0.1:7860"
ASSETS_DIR = Path(r"C:\Games\VisualNovel\assets\characters")
LOG_DIR = Path(r"C:\Games\VisualNovel\test_sprites")
LOG_FILE = LOG_DIR / "generation_v2_log.md"

# ============================================================================
# Generation Settings
# ============================================================================

QUALITY_PREFIX = (
    "masterpiece, best quality, detailed face, portrait, upper body, half body, "
    "looking at viewer, muted colors, 1920s germany, oil painting style, "
    "dramatic lighting, cinematic"
)

POSE_LOCK = "front view, facing viewer, centered composition, symmetrical face"

BG_POSITIVE = ", simple background, white background, solid color background, plain white background"

COMMON_NEGATIVE = (
    "lowres, bad anatomy, bad hands, text, error, missing fingers, "
    "extra digit, fewer digits, cropped, worst quality, low quality, "
    "normal quality, jpeg artifacts, signature, watermark, username, blurry, "
    "3d render, bright neon colors"
)

BG_NEGATIVE = (
    ", dark background, black background, grey background, "
    "detailed background, side view, profile, turned away"
)

GENERATION = {
    "steps": 28,
    "cfg_scale": 7,
    "width": 832,
    "height": 1216,
    "sampler_name": "DPM++ 2M SDE",
    "scheduler": "Karras",
}

DENOISING_STRENGTH = 0.65
REMBG_MODEL = "isnet-anime"

# ============================================================================
# Charakter-Definitionen
# ============================================================================

CHARACTERS = {
    "elise": {
        "name": "Elise Brandt",
        "seed": 42,
        "identity": (
            "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
            "brown eyes, slender, pale skin, "
            "1920s german clothing, long dark coat, high collar blouse, "
            "serious intellectual look"
        ),
        "negative_extra": ", multiple girls, male, child, modern clothing, wings",
        "expressions": {
            "neutral": "neutral expression, calm face, composed",
            "happy": "happy expression, bright smile, squinting happy eyes, warm cheerful face",
            "sad": "sad expression, downturned mouth, downcast sorrowful eyes, heavy brow, melancholic",
            "afraid": "very frightened expression, wide open eyes, open mouth gasping, pale face, trembling",
            "angry": "angry expression, deep frown, furrowed eyebrows, clenched jaw, intense glare",
            "shocked": "shocked expression, very wide eyes, open mouth gasping, raised eyebrows, stunned",
            "thinking": "thoughtful expression, eyes looking up, slightly pursed lips, raised eyebrow",
            "determined": "determined expression, firm set jaw, narrowed focused eyes, resolute stare",
            "worried": "worried expression, furrowed brow, anxious wide eyes, biting lower lip, tense",
        },
    },
    "georg": {
        "name": "Georg Brandt",
        "seed": 100,
        "identity": (
            "1man, solo, 45 years old, strong build, blacksmith, dark hair graying, "
            "weathered skin, calloused hands, simple work clothing, leather apron, "
            "broad shoulders, tired eyes, moustache"
        ),
        "negative_extra": ", woman, child, young, modern clothing, slim, clean",
        "expressions": {
            "neutral": "neutral expression, stoic face, calm",
            "guilty": "guilty expression, eyes looking down, furrowed brow, frowning, pained face",
            "angry": "very angry expression, gritting teeth, deep frown, furrowed eyebrows, intense glare, rage",
            "sad": "very sad expression, downturned mouth, sorrowful eyes looking down, heavy brow, melancholic",
            "determined": "determined expression, clenched jaw, narrowed eyes, intense focused stare",
            "afraid": "very frightened expression, wide open eyes, open mouth, pale face, horror, sweating",
            "protective": "fierce protective expression, gritted teeth, intense glaring eyes, aggressive scowl",
        },
    },
    "konrad": {
        "name": "Konrad Messer",
        "seed": 2200,
        "denoising": 0.7,
        "identity": (
            "1man, solo, 30 years old, handsome face, warm brown eyes, wavy dark hair, "
            "teacher clothing 1920s, vest, rolled up sleeves, "
            "fit build, friendly appearance"
        ),
        "negative_extra": ", woman, child, old, fat, modern clothing",
        "expressions": {
            "neutral": "neutral expression, calm pleasant face, relaxed",
            "charming": "charming expression, warm wide smile, inviting bright eyes, head slightly tilted",
            "suspicious": "suspicious expression, narrowed eyes, one raised eyebrow, tight lipped smirk",
            "dark": "dark sinister expression, shadowed eyes, eerie cold stare, unsettling grin, menacing",
            "possessed": "possessed expression, unnaturally wide eyes, glowing pupils, twisted smile, dark aura",
            "sad": "sad expression, downturned mouth, sorrowful eyes, furrowed brow, pained look",
            "smiling": "gentle warm smile, soft relaxed eyes, kind reassuring face",
        },
    },
    "voss": {
        "name": "Pastor Friedrich Voss",
        "seed": 300,
        "identity": (
            "1man, solo, 55 years old, gaunt face, hollow cheeks, thin gray hair, "
            "deep set dark eyes, bags under eyes, black pastor robes, white collar, "
            "lutheran pastor, emaciated, haunted look, wrinkled skin"
        ),
        "negative_extra": ", woman, child, young, muscular, fat, modern clothing",
        "expressions": {
            "neutral": "neutral expression, weary tired eyes, gaunt face",
            "worried": "worried expression, deeply furrowed brow, wide anxious eyes, tense mouth",
            "angry": "very angry expression, gritting teeth, furrowed brow, intense burning eyes, furious",
            "afraid": "terrified expression, very wide horrified eyes, open mouth gasping, pale face, sweating",
            "praying": "praying expression, eyes tightly shut, pained anguished face, bowed head",
            "broken": "broken expression, hollow vacant eyes, slack jaw, tear streaks, utterly defeated",
            "warning": "warning expression, wide urgent eyes, open mouth shouting, raised eyebrows, alarmed",
        },
    },
    "anna": {
        "name": "Anna",
        "seed": 400,
        "identity": (
            "1girl, solo, 19 years old, pale blonde hair, very pale skin, "
            "light blue eyes, ethereal appearance, thin, simple white dress, "
            "distant look, dark circles under eyes, otherworldly beauty"
        ),
        "negative_extra": ", man, child, old, modern clothing, tan skin",
        "expressions": {
            "neutral": "neutral expression, distant gaze, slightly unfocused eyes",
            "dreamy": "dreamy expression, faraway half-closed eyes, faint gentle smile, unfocused",
            "afraid": "afraid expression, very wide frightened eyes, trembling lip, clutching self",
            "drawing": "focused expression, eyes looking down concentrated, slight frown, absorbed",
            "possessed": "possessed expression, unnaturally wide blank eyes, frozen face, eerie stillness",
            "lucid": "lucid expression, clear focused eyes, slightly open mouth, urgent aware look",
            "crying": "crying expression, tears streaming down face, red puffy eyes, sobbing",
        },
    },
    "hilde": {
        "name": "Hilde Wurzel",
        "seed": 500,
        "identity": (
            "1woman, solo, 68 years old, elderly, white braided hair, weathered face, "
            "green eyes, wise look, herbalist clothing, apron, dried herbs, "
            "sturdy build, earth tones, wrinkled hands"
        ),
        "negative_extra": ", man, child, young, modern clothing, fantasy robes",
        "expressions": {
            "neutral": "neutral expression, calm observant eyes, composed face",
            "wise": "wise expression, warm knowing smile, crinkled eyes, raised eyebrow",
            "warning": "warning expression, wide serious eyes, open mouth, urgent frown, raised eyebrows",
            "kind": "kind expression, big warm smile, soft squinting eyes, gentle grandmother face",
            "mysterious": "mysterious expression, slight smirk, half-closed eyes, enigmatic knowing look",
            "ritual": "focused intense expression, narrowed concentrated eyes, determined set mouth, serious",
            "angry": "very angry expression, deep furrowed brow, gritting teeth, fierce glare, scowling",
        },
    },
    "otto": {
        "name": "Buergermeister Otto Krug",
        "seed": 600,
        "denoising": 0.7,
        "identity": (
            "1man, solo, 60 years old, heavy set, gray hair slicked back, "
            "thick moustache, ruddy face, mayor clothing 1920s, formal suit, "
            "vest, tie, large build, double chin"
        ),
        "negative_extra": ", woman, child, young, slim, modern clothing, clock, pocket watch",
        "expressions": {
            "neutral": "neutral expression, calculating eyes, calm composed face",
            "authoritative": "authoritative expression, raised chin, stern frown, looking down, commanding",
            "threatening": "very threatening expression, narrowed eyes, sinister scowl, clenched jaw, menacing",
            "jovial": "very happy expression, wide open mouth laughing, big smile, squinting eyes, rosy cheeks, hearty laugh",
            "angry": "very angry expression, shouting, wide open mouth yelling, deep red face, bulging veins, furious rage",
            "desperate": "desperate expression, wide panicked eyes, sweating, open mouth gasping, disheveled, losing composure",
        },
    },
    "margarethe": {
        "name": "Margarethe",
        "seed": 700,
        "identity": (
            "1woman, solo, 78 years old, very elderly, white thin hair in bun, "
            "deeply wrinkled face, kind but knowing eyes, dark shawl, "
            "traditional german grandmother clothing, frail frame"
        ),
        "negative_extra": ", man, child, young, modern clothing",
        "denoising_overrides": {"young": 0.80, "ghostly": 0.75},
        "expressions": {
            "neutral": "neutral expression, gentle calm face, soft eyes",
            "kind": "kind expression, warm wide smile, soft crinkled eyes, gentle grandmother face",
            "warning": "warning expression, wide frightened eyes, open mouth, urgent pleading face",
            "sad": "very sad expression, teary glistening eyes, downturned trembling mouth, deep grief",
            "young": "younger version, 40 years old, same features but less wrinkled, dark hair",
            "ghostly": "ghostly appearance, transparent, ethereal glow, spirit form, pale glowing eyes",
        },
    },
}

# ============================================================================
# Funktionen
# ============================================================================

def log(msg: str):
    print(msg, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def img_to_base64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


def switch_to_animagine() -> bool:
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/options", timeout=10)
        current = r.json().get("sd_model_checkpoint", "")
        if "animagine" in current.lower():
            log(f"Animagine bereits geladen: {current}")
            return True

        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=10)
        for m in r.json():
            if "animagine" in m["model_name"].lower():
                log(f"Wechsle zu {m['title']}...")
                requests.post(f"{SD_URL}/sdapi/v1/options",
                              json={"sd_model_checkpoint": m["title"]}, timeout=180)
                time.sleep(5)
                log(f"Modell geladen.")
                return True
        log("FEHLER: Animagine nicht gefunden!")
        return False
    except Exception as e:
        log(f"FEHLER: {e}")
        return False


_rembg_session = None

def get_rembg_session():
    global _rembg_session
    if _rembg_session is None:
        from rembg import new_session
        log(f"Lade rembg Modell: {REMBG_MODEL}...")
        _rembg_session = new_session(REMBG_MODEL)
        log(f"{REMBG_MODEL} geladen.")
    return _rembg_session


def process_with_rembg(img: Image.Image) -> Image.Image:
    from rembg import remove
    session = get_rembg_session()
    return remove(img, session=session)


def crop_to_sprite(img: Image.Image) -> Image.Image:
    w, h = img.size
    crop_top = 0
    crop_bottom = int(h * 0.88)
    crop_left = int(w * 0.08)
    crop_right = w - int(w * 0.08)
    cropped = img.crop((crop_left, crop_top, crop_right, crop_bottom))

    target_w, target_h = 600, 900
    img_ratio = cropped.width / cropped.height
    target_ratio = target_w / target_h
    if img_ratio > target_ratio:
        new_w = target_w
        new_h = int(target_w / img_ratio)
    else:
        new_h = target_h
        new_w = int(target_h * img_ratio)
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    x_offset = (target_w - new_w) // 2
    y_offset = target_h - new_h
    canvas.paste(resized, (x_offset, y_offset))
    return canvas


def build_prompt(char: dict, expression_prompt: str) -> tuple[str, str]:
    prompt = (f"{QUALITY_PREFIX}, {char['identity']}, {POSE_LOCK}, "
              f"{expression_prompt}{BG_POSITIVE}")
    negative = COMMON_NEGATIVE + char.get("negative_extra", "") + BG_NEGATIVE
    return prompt, negative


def generate_reference(char_id: str, char: dict) -> Image.Image:
    """Generiert das Referenzbild (neutral) per txt2img."""
    neutral_expr = char["expressions"].get("neutral", list(char["expressions"].values())[0])
    prompt, negative = build_prompt(char, neutral_expr)

    payload = {
        **GENERATION,
        "prompt": prompt,
        "negative_prompt": negative,
        "batch_size": 1,
        "n_iter": 1,
        "seed": char["seed"],
    }

    log(f"  Referenzbild (neutral, txt2img, seed={char['seed']})...")
    t0 = time.time()
    r = requests.post(f"{SD_URL}/sdapi/v1/txt2img", json=payload, timeout=300)
    dt = round(time.time() - t0, 1)

    if r.status_code != 200:
        log(f"    FEHLER: API {r.status_code}")
        return None

    data = r.json()
    img_data = base64.b64decode(data["images"][0])
    img = Image.open(io.BytesIO(img_data))
    log(f"    Referenz generiert in {dt}s")
    return img


def generate_expression(ref_img: Image.Image, char: dict,
                        expression: str, denoising: float) -> Image.Image:
    """Generiert eine Expression per img2img vom Referenzbild."""
    expr_prompt = char["expressions"][expression]
    prompt, negative = build_prompt(char, expr_prompt)

    payload = {
        "init_images": [img_to_base64(ref_img)],
        "prompt": prompt,
        "negative_prompt": negative,
        "steps": GENERATION["steps"],
        "cfg_scale": GENERATION["cfg_scale"],
        "width": GENERATION["width"],
        "height": GENERATION["height"],
        "sampler_name": GENERATION["sampler_name"],
        "scheduler": GENERATION["scheduler"],
        "seed": char["seed"],
        "denoising_strength": denoising,
    }

    r = requests.post(f"{SD_URL}/sdapi/v1/img2img", json=payload, timeout=300)
    if r.status_code != 200:
        return None

    data = r.json()
    img_data = base64.b64decode(data["images"][0])
    return Image.open(io.BytesIO(img_data))


def generate_character(char_id: str, char: dict, output_dir: Path,
                       expressions: list = None, keep_raw: bool = False,
                       denoising: float = DENOISING_STRENGTH) -> list:
    """Generiert alle Sprites fuer einen Charakter."""
    output_dir.mkdir(parents=True, exist_ok=True)
    results = []

    exprs = expressions or list(char["expressions"].keys())
    exprs = [e for e in exprs if e in char["expressions"]]

    # Schritt 1: Referenzbild generieren (neutral, txt2img)
    ref_img = generate_reference(char_id, char)
    if ref_img is None:
        log(f"    FEHLER: Referenzbild konnte nicht generiert werden!")
        return results

    if keep_raw:
        raw_dir = LOG_DIR / f"{char_id}_raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        ref_img.save(raw_dir / f"{char_id}_reference.png")

    # Schritt 2: Neutral-Sprite direkt vom Referenzbild erstellen
    if "neutral" in exprs:
        t0 = time.time()
        try:
            nobg = process_with_rembg(ref_img)
            sprite = crop_to_sprite(nobg)
            sprite.save(output_dir / f"{char_id}_neutral.png")
            dt_bg = round(time.time() - t0, 1)
            log(f"  neutral: OK (ref, {dt_bg}s bg)")
            results.append({"character": char_id, "expression": "neutral",
                           "success": True, "method": "txt2img_ref"})
        except Exception as e:
            log(f"  neutral: FEHLER {e}")
            results.append({"character": char_id, "expression": "neutral",
                           "success": False, "error": str(e)})

    # Schritt 3: Alle anderen Expressions per img2img
    other_exprs = [e for e in exprs if e != "neutral"]
    for expr in other_exprs:
        expr_dns = char.get("denoising_overrides", {}).get(expr, denoising)
        log(f"  {expr} (img2img, dns={expr_dns})...")
        t0 = time.time()

        try:
            img = generate_expression(ref_img, char, expr, expr_dns)
            dt_gen = round(time.time() - t0, 1)

            if img is None:
                log(f"    FEHLER: img2img fehlgeschlagen")
                results.append({"character": char_id, "expression": expr,
                               "success": False, "error": "img2img failed"})
                continue

            if keep_raw:
                img.save(raw_dir / f"{char_id}_{expr}_raw.png")

            t1 = time.time()
            nobg = process_with_rembg(img)
            sprite = crop_to_sprite(nobg)
            sprite.save(output_dir / f"{char_id}_{expr}.png")
            dt_bg = round(time.time() - t1, 1)

            log(f"    OK ({dt_gen}s gen, {dt_bg}s bg)")
            results.append({"character": char_id, "expression": expr,
                           "success": True, "time_gen": dt_gen, "time_bg": dt_bg,
                           "method": "img2img"})

        except Exception as e:
            log(f"    FEHLER: {e}")
            results.append({"character": char_id, "expression": expr,
                           "success": False, "error": str(e)})

        time.sleep(1)

    return results


def main():
    parser = argparse.ArgumentParser(description="Generiere Charakter-Sprites (img2img)")
    parser.add_argument("--characters", nargs="*", default=None,
                        help="Nur bestimmte Charaktere (z.B. elise georg)")
    parser.add_argument("--expressions", nargs="*", default=None,
                        help="Nur bestimmte Expressions")
    parser.add_argument("--keep-raw", action="store_true",
                        help="Raw-Bilder in test_sprites/ behalten")
    parser.add_argument("--test-dir", action="store_true",
                        help="Sprites nach test_sprites/ statt assets/characters/")
    parser.add_argument("--denoising", type=float, default=DENOISING_STRENGTH,
                        help=f"Denoising Strength (default: {DENOISING_STRENGTH})")
    args = parser.parse_args()

    # API Check
    try:
        if not requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5).ok:
            print("FEHLER: API nicht erreichbar")
            sys.exit(1)
    except Exception:
        print("FEHLER: API nicht erreichbar - ist Forge gestartet?")
        sys.exit(1)

    requests.post(f"{SD_URL}/sdapi/v1/refresh-checkpoints", timeout=30)
    time.sleep(2)

    chars_to_gen = args.characters or list(CHARACTERS.keys())
    chars_to_gen = [c for c in chars_to_gen if c in CHARACTERS]

    if not chars_to_gen:
        print("Keine gueltigen Charaktere!")
        sys.exit(1)

    # Zaehlen
    total = 0
    for cid in chars_to_gen:
        exprs = args.expressions or list(CHARACTERS[cid]["expressions"].keys())
        exprs = [e for e in exprs if e in CHARACTERS[cid]["expressions"]]
        total += len(exprs)

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Charakter-Sprite Generierung V2 (img2img)\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Methode: txt2img Referenz + img2img Expressions\n")
        f.write(f"Denoising: {args.denoising}\n")
        f.write(f"rembg: {REMBG_MODEL}\n")
        f.write(f"Charaktere: {', '.join(chars_to_gen)}\n")
        f.write(f"Total Sprites: {total}\n\n")

    log(f"=== Generiere {total} Sprites fuer {len(chars_to_gen)} Charaktere ===")
    log(f"Methode: img2img (Denoising {args.denoising})\n")

    if not switch_to_animagine():
        sys.exit(1)

    all_results = []

    for cid in chars_to_gen:
        char = CHARACTERS[cid]
        exprs = args.expressions or list(char["expressions"].keys())
        exprs = [e for e in exprs if e in char["expressions"]]

        if args.test_dir:
            output_dir = LOG_DIR / cid
        else:
            output_dir = ASSETS_DIR / cid

        log(f"\n{'='*60}")
        log(f"{char['name']} ({cid}) - {len(exprs)} Expressions")
        log(f"Seed: {char['seed']}, Output: {output_dir}")
        log(f"{'='*60}")

        char_dns = char.get("denoising", args.denoising)
        results = generate_character(cid, char, output_dir, exprs,
                                     args.keep_raw, char_dns)
        all_results.extend(results)

    # Zusammenfassung
    log(f"\n{'='*60}")
    log(f"ZUSAMMENFASSUNG")
    log(f"{'='*60}\n")

    success = sum(1 for r in all_results if r["success"])
    failed = sum(1 for r in all_results if not r["success"])
    log(f"Gesamt: {success}/{len(all_results)} erfolgreich, {failed} fehlgeschlagen\n")

    for cid in chars_to_gen:
        cr = [r for r in all_results if r["character"] == cid]
        ok = sum(1 for r in cr if r["success"])
        log(f"**{CHARACTERS[cid]['name']}**: {ok}/{len(cr)} OK")

    if failed > 0:
        log(f"\n### Fehlgeschlagen:")
        for r in all_results:
            if not r["success"]:
                log(f"- {r['character']}/{r['expression']}: {r.get('error', '?')}")

    json_path = LOG_DIR / "generation_v2_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    log(f"\nJSON: {json_path}")


if __name__ == "__main__":
    main()
