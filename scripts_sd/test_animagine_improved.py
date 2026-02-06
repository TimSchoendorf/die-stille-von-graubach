"""
Animagine XL 3.1 - Verbesserter Oil Painting Test
===================================================
Basierend auf User-Feedback:
- Animagine Oil hatte beste Charakter-Konsistenz
- PROBLEM: "dark atmosphere" erzeugte dunklen BG -> rembg versagte
- FIX: dark atmosphere entfernt, heller BG forciert, dark bg im Negative
- FIX: 832x1216 Portrait statt 1024x1024
- 6 Expressions, mehrere BG-Varianten
"""
import base64
import io
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from PIL import Image

SD_URL = "http://127.0.0.1:7860"
TEST_DIR = Path(r"C:\Games\VisualNovel\test_sprites")
LOG_FILE = TEST_DIR / "animagine_improved_log.md"

# ============================================================================
# Charakter-Identitaet (Original Animagine Tags - funktionierte gut!)
# ============================================================================

ELISE_IDENTITY = (
    "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
    "brown eyes, slender, pale skin, "
    "1920s german clothing, long dark coat, high collar blouse, "
    "serious intellectual look"
)

ELISE_NEGATIVE = (
    "lowres, bad anatomy, bad hands, text, error, missing fingers, "
    "extra digit, fewer digits, cropped, worst quality, low quality, "
    "normal quality, jpeg artifacts, signature, watermark, username, blurry, "
    "3d render, bright neon colors, multiple girls, male, child"
)

EXPRESSIONS = {
    "neutral": "neutral expression, calm face",
    "happy": "gentle smile, warm expression",
    "afraid": "frightened expression, wide eyes, trembling",
    "sad": "sad expression, downcast eyes, melancholy",
    "angry": "angry expression, furrowed brows, intense",
    "shocked": "shocked expression, wide eyes, open mouth, gasping",
}

# ============================================================================
# Test-Konfigurationen - Alle Animagine XL Oil Painting
# ============================================================================

CONFIGS = {
    "a1_oil_whitebg": {
        "description": "Animagine Oil - OHNE dark atmosphere, white BG",
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting",
        "bg": ", simple background, white background",
        "negative_extra": ", dark background, black background, grey background",
        "width": 832,
        "height": 1216,
        "cfg": 7,
    },
    "a2_oil_strongbg": {
        "description": "Animagine Oil - Verstaerkter weisser BG",
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", simple background, white background, solid color background, plain white background",
        "negative_extra": ", dark background, black background, grey background, "
                         "gradient background, detailed background",
        "width": 832,
        "height": 1216,
        "cfg": 7,
    },
    "a3_oil_1024": {
        "description": "Animagine Oil - Original 1024x1024, aber OHNE dark atmosphere",
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting",
        "bg": ", simple background, white background",
        "negative_extra": ", dark background, black background, grey background",
        "width": 1024,
        "height": 1024,
        "cfg": 7,
    },
    "a4_oil_cfg8": {
        "description": "Animagine Oil - CFG 8 (staerkere Prompt-Befolgung)",
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting",
        "bg": ", simple background, white background",
        "negative_extra": ", dark background, black background, grey background",
        "width": 832,
        "height": 1216,
        "cfg": 8,
    },
}

# ============================================================================
# Funktionen
# ============================================================================

def log(msg: str):
    print(msg, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def switch_to_animagine() -> bool:
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/options", timeout=10)
        current = r.json().get("sd_model_checkpoint", "")
        if "animagine" in current.lower():
            log(f"  Animagine bereits geladen: {current}")
            return True

        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=10)
        for m in r.json():
            if "animagine" in m["model_name"].lower():
                log(f"  Wechsle zu {m['title']}...")
                requests.post(f"{SD_URL}/sdapi/v1/options",
                              json={"sd_model_checkpoint": m["title"]}, timeout=180)
                time.sleep(5)
                log(f"  Modell geladen.")
                return True
        log("  FEHLER: Animagine nicht gefunden!")
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


def crop_to_sprite(img: Image.Image, source_w: int, source_h: int) -> Image.Image:
    """Konsistentes Cropping mit angepasstem Fenster je nach Quellformat."""
    w, h = img.size

    if source_w == source_h:
        # 1024x1024: Mehr vom oberen/unteren Rand abschneiden
        crop_top = int(h * 0.02)
        crop_bottom = int(h * 0.92)
        crop_left = int(w * 0.10)
        crop_right = w - int(w * 0.10)
    else:
        # 832x1216 Portrait: Standard-Fenster
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

    prompt = f"{config['quality']}, {ELISE_IDENTITY}, {EXPRESSIONS[expression]}{config['bg']}"
    negative = ELISE_NEGATIVE + config.get("negative_extra", "")

    payload = {
        "prompt": prompt,
        "negative_prompt": negative,
        "steps": 28,
        "cfg_scale": config["cfg"],
        "width": config["width"],
        "height": config["height"],
        "sampler_name": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "batch_size": 1,
        "n_iter": 1,
        "seed": seed,
    }

    log(f"  {expression} (seed={seed}, cfg={config['cfg']}, {config['width']}x{config['height']})...")

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
        sprite = crop_to_sprite(img_nobg, config["width"], config["height"])
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

    try:
        if not requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5).ok:
            print("FEHLER: API nicht erreichbar")
            sys.exit(1)
    except Exception:
        print("FEHLER: API nicht erreichbar - ist Forge gestartet?")
        sys.exit(1)

    # Modell-Refresh
    requests.post(f"{SD_URL}/sdapi/v1/refresh-checkpoints", timeout=30)
    time.sleep(2)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Animagine XL 3.1 Improved Oil Painting Test\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Charakter: Elise\n")
        f.write(f"Expressions: {', '.join(args.expressions)}\n")
        f.write(f"Seed: {args.seed}\n\n")
        f.write(f"## Aenderungen gegenueber Original\n")
        f.write(f"- 'dark atmosphere' ENTFERNT (war Ursache fuer dunkle BGs)\n")
        f.write(f"- 832x1216 Portrait Format (statt 1024x1024)\n")
        f.write(f"- 'dark background' im Negative Prompt\n")
        f.write(f"- Verstaerkte BG-Anweisungen getestet\n")
        f.write(f"- 6 Expressions statt 3\n\n")

    if not switch_to_animagine():
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
        if cfg_name not in CONFIGS:
            continue
        cr = [r for r in all_results if r["config"] == cfg_name]
        ok = sum(1 for r in cr if r["success"])
        log(f"\n**{cfg_name}**: {ok}/{len(cr)} OK")

    json_path = TEST_DIR / "animagine_improved_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    log(f"\nJSON: {json_path}")


if __name__ == "__main__":
    main()
