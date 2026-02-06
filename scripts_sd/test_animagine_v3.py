"""
Animagine XL 3.1 - V3 Optimierung
==================================
Basierend auf User-Feedback: a2_oil_strongbg ist der beste Stil.
Jetzt optimieren wir:
1. Bessere Hintergrund-Entfernung (isnet-anime, birefnet-portrait)
2. Mehr Konsistenz (Pose-Locking, Identity-Verstaerkung)
3. Verschiedene BG-Ansaetze (green screen, prompt weighting)
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
LOG_FILE = TEST_DIR / "v3_optimization_log.md"

# ============================================================================
# Charakter-Identitaet - Verstaerkt fuer mehr Konsistenz
# ============================================================================

# Original a2 Identity (funktioniert gut)
ELISE_BASE = (
    "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
    "brown eyes, slender, pale skin, "
    "1920s german clothing, long dark coat, high collar blouse, "
    "serious intellectual look"
)

# Verstaerkt: Pose-Locking + mehr Details
ELISE_CONSISTENT = (
    "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
    "brown eyes, slender, pale skin, "
    "1920s german clothing, long dark coat, high collar blouse, "
    "serious intellectual look, "
    "front view, facing viewer, centered composition, symmetrical face"
)

NEGATIVE_BASE = (
    "lowres, bad anatomy, bad hands, text, error, missing fingers, "
    "extra digit, fewer digits, cropped, worst quality, low quality, "
    "normal quality, jpeg artifacts, signature, watermark, username, blurry, "
    "3d render, bright neon colors, multiple girls, male, child"
)

EXPRESSIONS = {
    "neutral": "neutral expression, calm face, composed",
    "happy": "gentle smile, warm expression, soft eyes",
    "afraid": "frightened expression, wide eyes, trembling, fearful",
    "shocked": "shocked expression, wide eyes, open mouth, gasping",
}

# ============================================================================
# Test-Konfigurationen
# ============================================================================

CONFIGS = {
    # --- BG-Varianten (alle mit isnet-anime) ---
    "v1_isnet_anime": {
        "description": "a2 Basis + isnet-anime rembg (statt default u2net)",
        "identity": ELISE_BASE,
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", simple background, white background, solid color background, plain white background",
        "negative_extra": ", dark background, black background, grey background, "
                         "detailed background",
        "rembg_model": "isnet-anime",
        "cfg": 7,
    },
    "v2_birefnet": {
        "description": "a2 Basis + birefnet-portrait rembg",
        "identity": ELISE_BASE,
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", simple background, white background, solid color background, plain white background",
        "negative_extra": ", dark background, black background, grey background, "
                         "detailed background",
        "rembg_model": "birefnet-portrait",
        "cfg": 7,
    },
    "v3_green_screen": {
        "description": "Gruener Hintergrund + isnet-anime (Green Screen Ansatz)",
        "identity": ELISE_BASE,
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", simple background, green background, solid green background, chroma key",
        "negative_extra": ", detailed background, complex background",
        "rembg_model": "isnet-anime",
        "cfg": 7,
    },
    "v4_weighted_bg": {
        "description": "Prompt-Gewichtung fuer weissen BG + isnet-anime",
        "identity": ELISE_BASE,
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", (simple background, white background:1.4), solid color background",
        "negative_extra": ", (dark background, black background, grey background:1.3), "
                         "detailed background, gradient background",
        "rembg_model": "isnet-anime",
        "cfg": 7,
    },
    # --- Konsistenz-Varianten ---
    "v5_pose_locked": {
        "description": "Pose-Locking + isnet-anime (front view, centered, symmetrical)",
        "identity": ELISE_CONSISTENT,
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", simple background, white background, solid color background, plain white background",
        "negative_extra": ", dark background, black background, grey background, "
                         "detailed background, side view, profile, turned away",
        "rembg_model": "isnet-anime",
        "cfg": 7,
    },
    "v6_cfg9_locked": {
        "description": "CFG 9 + Pose-Lock + isnet-anime (maximale Prompt-Treue)",
        "identity": ELISE_CONSISTENT,
        "quality": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                   "looking at viewer, muted colors, 1920s germany, oil painting style, "
                   "dramatic lighting, cinematic",
        "bg": ", (simple background, white background:1.3), solid color background",
        "negative_extra": ", (dark background, black background, grey background:1.3), "
                         "detailed background, side view, profile, turned away",
        "rembg_model": "isnet-anime",
        "cfg": 9,
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


# Cache fuer rembg Sessions (Modell nur einmal laden)
_rembg_sessions = {}

def get_rembg_session(model_name: str):
    if model_name not in _rembg_sessions:
        from rembg import new_session
        log(f"    Lade rembg Modell: {model_name}...")
        _rembg_sessions[model_name] = new_session(model_name)
        log(f"    {model_name} geladen.")
    return _rembg_sessions[model_name]


def process_with_rembg(img: Image.Image, model_name: str = "u2net") -> Image.Image:
    try:
        from rembg import remove
        session = get_rembg_session(model_name)
        return remove(img, session=session)
    except Exception as e:
        log(f"    rembg FEHLER ({model_name}): {e}")
        return img.convert("RGBA")


def crop_to_sprite(img: Image.Image) -> Image.Image:
    """Konsistentes Cropping: Festes Fenster fuer 832x1216."""
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


def generate(config_name: str, config: dict, expression: str, seed: int = 42) -> dict:
    result = {
        "config": config_name,
        "expression": expression,
        "success": False,
        "time_gen": 0,
        "time_bg": 0,
        "seed": seed,
        "rembg_model": config.get("rembg_model", "u2net"),
        "error": "",
    }

    out_dir = TEST_DIR / config_name
    out_dir.mkdir(parents=True, exist_ok=True)

    prompt = (f"{config['quality']}, {config['identity']}, "
              f"{EXPRESSIONS[expression]}{config['bg']}")
    negative = NEGATIVE_BASE + config.get("negative_extra", "")

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

    rembg_model = config.get("rembg_model", "u2net")
    log(f"  {expression} (seed={seed}, cfg={config['cfg']}, rembg={rembg_model})...")

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
        img.save(out_dir / f"elise_{expression}_raw.png")
        log(f"    Generiert in {result['time_gen']}s")

    except Exception as e:
        result["error"] = str(e)
        log(f"    FEHLER: {e}")
        return result

    # rembg
    t1 = time.time()
    try:
        img_nobg = process_with_rembg(img, rembg_model)
        result["time_bg"] = round(time.time() - t1, 1)
        img_nobg.save(out_dir / f"elise_{expression}_nobg.png")
    except Exception as e:
        log(f"    rembg FEHLER: {e}")
        img_nobg = img.convert("RGBA")

    # Sprite
    try:
        sprite = crop_to_sprite(img_nobg)
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
                        default=["neutral", "happy", "afraid", "shocked"])
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    try:
        if not requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5).ok:
            print("FEHLER: API nicht erreichbar")
            sys.exit(1)
    except Exception:
        print("FEHLER: API nicht erreichbar - ist Forge gestartet?")
        sys.exit(1)

    requests.post(f"{SD_URL}/sdapi/v1/refresh-checkpoints", timeout=30)
    time.sleep(2)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Animagine V3 - Optimierung\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Basis: a2_oil_strongbg (User-Favorit)\n")
        f.write(f"Expressions: {', '.join(args.expressions)}\n")
        f.write(f"Seed: {args.seed}\n\n")
        f.write(f"## Test-Variablen\n")
        f.write(f"- rembg Modelle: isnet-anime, birefnet-portrait, u2net (default)\n")
        f.write(f"- BG: white, green screen, prompt-weighted\n")
        f.write(f"- Konsistenz: pose-locking, higher CFG\n\n")

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
    log(f"| Config | Expression | OK | Gen(s) | BG(s) | rembg |")
    log(f"|--------|-----------|-----|--------|-------|-------|")
    for r in all_results:
        ok = "Y" if r["success"] else "N"
        log(f"| {r['config']} | {r['expression']} | {ok} | {r['time_gen']} | {r['time_bg']} | {r['rembg_model']} |")

    for cfg_name in configs_to_run:
        if cfg_name not in CONFIGS:
            continue
        cr = [r for r in all_results if r["config"] == cfg_name]
        ok = sum(1 for r in cr if r["success"])
        log(f"\n**{cfg_name}**: {ok}/{len(cr)} OK")

    json_path = TEST_DIR / "v3_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    log(f"\nJSON: {json_path}")


if __name__ == "__main__":
    main()
