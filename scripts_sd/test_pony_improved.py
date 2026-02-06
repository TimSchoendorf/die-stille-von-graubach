"""
Pony V6 XL - Verbesserte Prompt-Tests
======================================
Basierend auf Erkenntnissen aus Test v2:
- Haar-Fix: "straight chin-length bob haircut" statt "bob hair"
- Kein "dark atmosphere" (erzeugt dunklen BG -> rembg versagt)
- Verbessertes Cropping (konsistente Positionierung)
- Verschiedene Prompt-Varianten
"""
import base64
import io
import json
import os
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

import requests
from PIL import Image

SD_URL = "http://127.0.0.1:7860"
TEST_DIR = Path(r"C:\Games\VisualNovel\test_sprites")
LOG_FILE = TEST_DIR / "pony_improved_log.md"

# ============================================================================
# Verbesserte Charakter-Identitaet
# ============================================================================

ELISE_IDENTITY_V2 = (
    "1girl, solo, 24 years old, straight chin-length bob haircut, dark brown hair, "
    "glasses, round glasses, brown eyes, slender, pale skin, "
    "1920s german clothing, long dark coat, high collar blouse, "
    "serious intellectual look"
)

ELISE_NEGATIVE = (
    "score_6, score_5, score_4, source_pony, source_furry, "
    "lowres, bad anatomy, bad hands, text, error, missing fingers, "
    "extra digit, fewer digits, cropped, worst quality, low quality, "
    "jpeg artifacts, signature, watermark, blurry, "
    "bright neon colors, multiple girls, male, child, "
    "curly hair, wavy hair, long hair"
)

EXPRESSIONS = {
    "neutral": "neutral expression, calm face, composed",
    "happy": "gentle smile, warm expression, soft eyes",
    "afraid": "frightened expression, wide eyes, trembling, fearful",
    "sad": "sad expression, downcast eyes, melancholy, sorrow",
    "angry": "angry expression, furrowed brows, clenched jaw, intense",
    "shocked": "shocked expression, wide eyes, open mouth, gasping",
}

# ============================================================================
# Test-Konfigurationen (alle Pony V6 XL)
# ============================================================================

CONFIGS = {
    "p1_realistic_clean": {
        "description": "Pony Realistic - Sauberer heller BG, kein dark atmosphere",
        "quality": "score_9, score_8_up, score_7_up, "
                   "detailed face, portrait, upper body, half body, "
                   "looking at viewer, dramatic lighting, cinematic, "
                   "oil painting style, muted colors, 1920s germany",
        "bg": ", simple background, white background",
        "cfg": 7,
    },
    "p2_realistic_plain": {
        "description": "Pony Realistic - Noch einfacherer BG, plain white",
        "quality": "score_9, score_8_up, score_7_up, "
                   "detailed face, portrait, upper body, half body, "
                   "looking at viewer, dramatic lighting, "
                   "oil painting style, muted colors",
        "bg": ", plain white background, solid color background",
        "cfg": 7,
    },
    "p3_anime_style": {
        "description": "Pony Anime - Visual Novel Stil",
        "quality": "score_9, score_8_up, score_7_up, source_anime, "
                   "detailed face, portrait, upper body, half body, "
                   "looking at viewer, dramatic lighting, "
                   "muted colors, visual novel",
        "bg": ", simple background, white background",
        "cfg": 7,
    },
    "p4_cfg6": {
        "description": "Pony Realistic - CFG 6 (weniger strikt)",
        "quality": "score_9, score_8_up, score_7_up, "
                   "detailed face, portrait, upper body, half body, "
                   "looking at viewer, dramatic lighting, cinematic, "
                   "oil painting style, muted colors, 1920s germany",
        "bg": ", simple background, white background",
        "cfg": 6,
    },
}

# ============================================================================
# Funktionen
# ============================================================================

def log(msg: str):
    print(msg, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def switch_to_pony() -> bool:
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/options", timeout=10)
        current = r.json().get("sd_model_checkpoint", "")
        if "pony" in current.lower():
            log(f"  Pony bereits geladen: {current}")
            return True

        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=10)
        for m in r.json():
            if "pony" in m["model_name"].lower():
                log(f"  Wechsle zu {m['title']}...")
                requests.post(f"{SD_URL}/sdapi/v1/options",
                              json={"sd_model_checkpoint": m["title"]}, timeout=180)
                time.sleep(5)
                log(f"  Modell geladen.")
                return True
        log("  FEHLER: Pony nicht gefunden!")
        return False
    except Exception as e:
        log(f"  FEHLER: {e}")
        return False


def process_with_rembg(img: Image.Image) -> Image.Image:
    try:
        from rembg import remove
        return remove(img)
    except ImportError:
        log("  WARNUNG: rembg nicht verfuegbar!")
        return img.convert("RGBA")


def crop_to_sprite_consistent(img: Image.Image) -> Image.Image:
    """Konsistentes Cropping: Festes Fenster, kein adaptives Bounding-Box."""
    w, h = img.size

    # Festes oberes 85% des Bildes nehmen, 10% Rand links/rechts
    crop_top = 0
    crop_bottom = int(h * 0.88)
    crop_left = int(w * 0.08)
    crop_right = w - int(w * 0.08)

    cropped = img.crop((crop_left, crop_top, crop_right, crop_bottom))

    # Auf 600x900 skalieren (Seitenverhaeltnis beibehalten)
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

    # Auf transparentem Canvas zentriert am unteren Rand platzieren
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    x_offset = (target_w - new_w) // 2
    y_offset = target_h - new_h
    canvas.paste(resized, (x_offset, y_offset))

    return canvas


def generate(config_name: str, config: dict, expression: str, seed: int = 42) -> dict:
    result = {
        "config": config_name,
        "expression": expression,
        "success": False,
        "time_gen": 0,
        "time_bg": 0,
        "seed": seed,
        "error": "",
    }

    out_dir = TEST_DIR / config_name
    out_dir.mkdir(parents=True, exist_ok=True)

    prompt = f"{config['quality']}, {ELISE_IDENTITY_V2}, {EXPRESSIONS[expression]}{config['bg']}"
    negative = ELISE_NEGATIVE

    payload = {
        "prompt": prompt,
        "negative_prompt": negative,
        "steps": 28,
        "cfg_scale": config["cfg"],
        "width": 832,
        "height": 1216,
        "sampler_name": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "batch_size": 1,
        "n_iter": 1,
        "seed": seed,
    }

    log(f"  {expression} (seed={seed}, cfg={config['cfg']})...")

    # Generierung
    t0 = time.time()
    try:
        r = requests.post(f"{SD_URL}/sdapi/v1/txt2img", json=payload, timeout=300)
        result["time_gen"] = round(time.time() - t0, 1)

        if r.status_code != 200:
            result["error"] = f"API {r.status_code}: {r.text[:200]}"
            log(f"    FEHLER: {result['error']}")
            return result

        data = r.json()
        info = json.loads(data.get("info", "{}"))
        result["seed"] = info.get("seed", seed)

        img_data = base64.b64decode(data["images"][0])
        img = Image.open(io.BytesIO(img_data))

        # Raw speichern
        img.save(out_dir / f"elise_{expression}_raw.png")
        log(f"    Generiert in {result['time_gen']}s")

    except Exception as e:
        result["error"] = str(e)
        log(f"    FEHLER: {e}")
        return result

    # rembg
    t1 = time.time()
    try:
        img_nobg = process_with_rembg(img)
        result["time_bg"] = round(time.time() - t1, 1)
        img_nobg.save(out_dir / f"elise_{expression}_nobg.png")
    except Exception as e:
        log(f"    rembg FEHLER: {e}")
        img_nobg = img.convert("RGBA")

    # Sprite
    try:
        sprite = crop_to_sprite_consistent(img_nobg)
        sprite.save(out_dir / f"elise_{expression}.png")
        result["success"] = True
        log(f"    OK ({result['time_gen']}s gen, {result['time_bg']}s rembg)")
    except Exception as e:
        result["error"] = f"Crop: {e}"
        log(f"    Crop FEHLER: {e}")

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--configs", nargs="*", default=None)
    parser.add_argument("--expressions", nargs="*",
                        default=["neutral", "happy", "afraid", "sad", "angry", "shocked"])
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if not requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5).ok:
        print("FEHLER: API nicht erreichbar")
        sys.exit(1)

    # Modell-Refresh
    requests.post(f"{SD_URL}/sdapi/v1/refresh-checkpoints", timeout=30)
    time.sleep(2)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Pony V6 XL Improved Test\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Charakter: Elise (verbesserte Prompts)\n")
        f.write(f"Expressions: {', '.join(args.expressions)}\n")
        f.write(f"Seed: {args.seed}\n\n")
        f.write(f"## Verbesserungen gegenueber v2\n")
        f.write(f"- Haar: 'straight chin-length bob haircut' + 'curly hair, wavy hair' in negative\n")
        f.write(f"- Kein 'dark atmosphere' im Quality-Prefix\n")
        f.write(f"- Konsistentes Cropping (festes Fenster statt adaptive BBox)\n")
        f.write(f"- 6 Expressions statt 3\n\n")

    if not switch_to_pony():
        sys.exit(1)

    configs_to_run = args.configs or list(CONFIGS.keys())
    all_results = []

    for cfg_name in configs_to_run:
        if cfg_name not in CONFIGS:
            continue
        cfg = CONFIGS[cfg_name]
        log(f"\n{'='*60}")
        log(f"{cfg_name}: {cfg['description']}")
        log(f"{'='*60}")

        for expr in args.expressions:
            r = generate(cfg_name, cfg, expr, args.seed)
            all_results.append(r)
            time.sleep(2)

    # Zusammenfassung
    log(f"\n## Zusammenfassung\n")
    log(f"| Config | Expression | OK | Gen(s) | BG(s) |")
    log(f"|--------|-----------|-----|--------|-------|")
    for r in all_results:
        ok = "Y" if r["success"] else "N"
        log(f"| {r['config']} | {r['expression']} | {ok} | {r['time_gen']} | {r['time_bg']} |")

    for cfg_name in configs_to_run:
        cr = [r for r in all_results if r["config"] == cfg_name]
        ok = sum(1 for r in cr if r["success"])
        log(f"\n**{cfg_name}**: {ok}/{len(cr)} OK")

    json_path = TEST_DIR / "pony_improved_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    log(f"\nJSON: {json_path}")


if __name__ == "__main__":
    main()
