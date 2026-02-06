"""
Sprite Generation Test Suite v2
================================
Tests verschiedene Modelle und Prompting-Stile zur Charakter-Sprite-Generierung.
Alle verwenden rembg fuer Transparenz (LayerDiffusion API nicht via alwayson_scripts
erreichbar in Forge - wird separat getestet).

Getestete Konfigurationen:
1. Animagine XL 3.1 + rembg (Baseline, oil painting style)
2. Animagine XL 3.1 + rembg (anime style variant)
3. Pony Diffusion V6 XL + rembg (score tags, anime source)
4. Pony Diffusion V6 XL + rembg (score tags, realistic source)
5. FLUX.1 dev FP8 + rembg (natural language)

Testcharakter: Elise (3 Expressions: neutral, happy, afraid)
"""
import argparse
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
LOG_FILE = TEST_DIR / "generation_log.md"

# ============================================================================
# Character Identity Prompts
# ============================================================================

# Tag-basiert (fuer Animagine/Pony SDXL)
ELISE_IDENTITY_TAGS = (
    "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
    "brown eyes, slender, pale skin, 1920s german clothing, long dark coat, "
    "high collar blouse, serious intellectual look"
)

# Natuerliche Sprache (fuer FLUX)
ELISE_IDENTITY_NATURAL = (
    "A portrait of a young woman in her mid-twenties with a dark brown bob haircut "
    "and round glasses. She has brown eyes, pale skin, and a slender build. She wears "
    "a long dark coat over a high-collared blouse in the style of 1920s Germany. "
    "She has a serious, intellectual appearance."
)

EXPRESSIONS_TAGS = {
    "neutral": "neutral expression, calm face",
    "happy": "gentle smile, warm expression",
    "afraid": "frightened expression, wide eyes, trembling",
}

EXPRESSIONS_NATURAL = {
    "neutral": "Her face shows a calm, neutral expression with composed features.",
    "happy": "She has a gentle, warm smile with kind eyes.",
    "afraid": "Her eyes are wide with fright, her expression showing visible fear and tension.",
}

COMMON_NEGATIVE_SDXL = (
    "lowres, bad anatomy, bad hands, text, error, missing fingers, "
    "extra digit, fewer digits, cropped, worst quality, low quality, "
    "normal quality, jpeg artifacts, signature, watermark, username, blurry, "
    "3d render, bright neon colors, multiple girls, male, child"
)

# ============================================================================
# Test-Konfigurationen
# ============================================================================

CONFIGS = {
    # --- Animagine XL 3.1 ---
    "01_animagine_oil": {
        "description": "Animagine XL 3.1 - Oil Painting Style (Baseline)",
        "model_search": "animagine",
        "prompt_style": "tags",
        "sampler": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "steps": 28,
        "cfg": 7,
        "width": 1024,
        "height": 1024,
        "quality_prefix": "masterpiece, best quality, detailed face, portrait, upper body, half body, "
                          "looking at viewer, dark atmosphere, muted colors, 1920s germany, "
                          "oil painting style, dramatic lighting",
        "bg_suffix": ", simple background, white background",
        "negative_extra": "",
    },
    "02_animagine_anime": {
        "description": "Animagine XL 3.1 - Anime/VN Style",
        "model_search": "animagine",
        "prompt_style": "tags",
        "sampler": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "steps": 28,
        "cfg": 7,
        "width": 832,
        "height": 1216,
        "quality_prefix": "masterpiece, best quality, anime style, visual novel sprite, "
                          "detailed face, upper body, looking at viewer, "
                          "dark atmosphere, muted colors, 1920s germany, dramatic lighting",
        "bg_suffix": ", simple background, white background",
        "negative_extra": "realistic, photo, 3d, ",
    },

    # --- Pony Diffusion V6 XL ---
    "03_pony_anime": {
        "description": "Pony Diffusion V6 XL - Anime Source Tags",
        "model_search": "ponyDiffusion",
        "prompt_style": "pony_tags",
        "sampler": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "steps": 28,
        "cfg": 7,
        "width": 832,
        "height": 1216,
        "quality_prefix": "score_9, score_8_up, score_7_up, source_anime, "
                          "detailed face, portrait, upper body, half body, "
                          "looking at viewer, dark atmosphere, muted colors, "
                          "1920s germany, dramatic lighting",
        "bg_suffix": ", simple background, white background",
        "negative_extra": "score_6, score_5, score_4, source_pony, source_furry, ",
    },
    "04_pony_realistic": {
        "description": "Pony Diffusion V6 XL - Realistic/Filmisch",
        "model_search": "ponyDiffusion",
        "prompt_style": "pony_tags",
        "sampler": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "steps": 28,
        "cfg": 7,
        "width": 832,
        "height": 1216,
        "quality_prefix": "score_9, score_8_up, score_7_up, "
                          "detailed face, portrait, upper body, half body, "
                          "looking at viewer, dark atmosphere, muted colors, "
                          "1920s germany, oil painting style, dramatic lighting, cinematic",
        "bg_suffix": ", simple background, white background",
        "negative_extra": "score_6, score_5, score_4, source_pony, source_furry, anime, cartoon, ",
    },

    # --- FLUX.1 dev FP8 ---
    "05_flux_natural": {
        "description": "FLUX.1 dev FP8 - Natural Language Prompting",
        "model_search": "flux1",
        "prompt_style": "natural",
        "sampler": "Euler",
        "scheduler": "Simple",
        "steps": 20,
        "cfg": 1.0,
        "width": 832,
        "height": 1216,
        "quality_prefix": "",
        "bg_suffix": " She is standing against a plain solid white background.",
        "negative_extra": "",
    },
}

# ============================================================================
# Hilfsfunktionen
# ============================================================================

def log(msg: str):
    """Schreibe ins Log und auf stdout."""
    print(msg, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def check_api() -> bool:
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5)
        return r.status_code == 200
    except:
        return False


def get_current_model() -> str:
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/options", timeout=10)
        return r.json().get("sd_model_checkpoint", "unknown")
    except:
        return "unknown"


def switch_model(search_term: str) -> bool:
    """Modell wechseln. Gibt True zurueck wenn erfolgreich."""
    current = get_current_model()
    if search_term.lower() in current.lower():
        log(f"  Modell bereits geladen: {current}")
        return True

    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=10)
        models = r.json()
        for m in models:
            if search_term.lower() in m["model_name"].lower():
                log(f"  Wechsle zu Modell: {m['title']}...")
                requests.post(
                    f"{SD_URL}/sdapi/v1/options",
                    json={"sd_model_checkpoint": m["title"]},
                    timeout=180
                )
                time.sleep(5)
                log(f"  Modell geladen: {m['title']}")
                return True
        log(f"  FEHLER: Modell '{search_term}' nicht gefunden!")
        # Zeige verfuegbare Modelle
        log(f"  Verfuegbar: {[m['model_name'] for m in models]}")
        return False
    except Exception as e:
        log(f"  FEHLER beim Modellwechsel: {e}")
        return False


def build_prompt(config: dict, expression: str) -> tuple[str, str]:
    """Erstelle Prompt und Negative Prompt basierend auf Config."""
    style = config["prompt_style"]

    if style == "natural":
        # FLUX: natuerliche Sprache
        prompt = (
            f"{ELISE_IDENTITY_NATURAL} "
            f"{EXPRESSIONS_NATURAL[expression]} "
            f"Upper body portrait, looking at the viewer. "
            f"Dark, moody atmosphere with dramatic lighting, "
            f"reminiscent of 1920s Germany. Oil painting aesthetic."
            f"{config['bg_suffix']}"
        )
        negative = ""  # FLUX ignoriert negative prompts weitgehend
    elif style == "pony_tags":
        # Pony: score-Tags + Character-Tags
        prompt = (
            f"{config['quality_prefix']}, "
            f"{ELISE_IDENTITY_TAGS}, "
            f"{EXPRESSIONS_TAGS[expression]}"
            f"{config['bg_suffix']}"
        )
        negative = f"{config['negative_extra']}{COMMON_NEGATIVE_SDXL}"
    else:
        # Standard tag-basiert (Animagine etc.)
        prompt = (
            f"{config['quality_prefix']}, "
            f"{ELISE_IDENTITY_TAGS}, "
            f"{EXPRESSIONS_TAGS[expression]}"
            f"{config['bg_suffix']}"
        )
        negative = f"{config['negative_extra']}{COMMON_NEGATIVE_SDXL}"

    return prompt, negative


def build_payload(config: dict, prompt: str, negative: str) -> dict:
    """Erstelle API-Payload."""
    payload = {
        "prompt": prompt,
        "negative_prompt": negative,
        "steps": config["steps"],
        "cfg_scale": config["cfg"],
        "width": config["width"],
        "height": config["height"],
        "sampler_name": config["sampler"],
        "scheduler": config["scheduler"],
        "batch_size": 1,
        "n_iter": 1,
        "seed": 42,  # Fester Seed fuer Vergleichbarkeit
    }
    return payload


def process_with_rembg(img: Image.Image) -> Image.Image:
    """Hintergrund entfernen mit rembg."""
    try:
        from rembg import remove
        return remove(img)
    except ImportError:
        log("  WARNUNG: rembg nicht verfuegbar!")
        return img.convert("RGBA")


def crop_to_sprite(img: Image.Image) -> Image.Image:
    """Zuschneiden auf 600x900 Sprite-Format."""
    w, h = img.size
    # Finde den Charakter-Bereich (nicht-transparente Pixel)
    if img.mode == "RGBA":
        # Bounding Box der nicht-transparenten Pixel
        bbox = img.getbbox()
        if bbox:
            # Etwas Padding hinzufuegen
            pad = 20
            x1 = max(0, bbox[0] - pad)
            y1 = max(0, bbox[1] - pad)
            x2 = min(w, bbox[2] + pad)
            y2 = min(h, bbox[3] + pad)
            img = img.crop((x1, y1, x2, y2))

    # Resize auf 600x900 mit Seitenverhaeltnis beibehalten
    target_w, target_h = 600, 900
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h

    if img_ratio > target_ratio:
        # Bild ist breiter - nach Breite skalieren
        new_w = target_w
        new_h = int(target_w / img_ratio)
    else:
        # Bild ist hoeher - nach Hoehe skalieren
        new_h = target_h
        new_w = int(target_h * img_ratio)

    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Auf Canvas zentrieren
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    offset_x = (target_w - new_w) // 2
    offset_y = target_h - new_h  # Am unteren Rand ausrichten
    canvas.paste(img_resized, (offset_x, offset_y))

    return canvas


def generate_single(config_name: str, config: dict, expression: str) -> dict:
    """Generiere ein einzelnes Testbild."""
    result = {
        "config": config_name,
        "description": config["description"],
        "expression": expression,
        "success": False,
        "time_generate": 0,
        "time_rembg": 0,
        "prompt": "",
        "negative": "",
        "output_raw": "",
        "output_nobg": "",
        "output_final": "",
        "error": "",
        "seed": 42,
    }

    out_dir = TEST_DIR / config_name
    out_dir.mkdir(parents=True, exist_ok=True)

    prompt, negative = build_prompt(config, expression)
    result["prompt"] = prompt
    result["negative"] = negative

    payload = build_payload(config, prompt, negative)

    log(f"  Generiere {expression}...")
    log(f"    Prompt: {prompt[:150]}...")

    # 1. Generierung
    start = time.time()
    try:
        r = requests.post(f"{SD_URL}/sdapi/v1/txt2img", json=payload, timeout=300)
        gen_time = time.time() - start
        result["time_generate"] = round(gen_time, 1)

        if r.status_code != 200:
            result["error"] = f"API Status {r.status_code}: {r.text[:300]}"
            log(f"    FEHLER: {result['error']}")
            return result

        data = r.json()
        # Seed aus Info extrahieren
        info = json.loads(data.get("info", "{}"))
        result["seed"] = info.get("seed", 42)

        img_data = base64.b64decode(data["images"][0])
        img = Image.open(io.BytesIO(img_data))

        # Raw speichern
        raw_path = out_dir / f"elise_{expression}_raw.png"
        img.save(raw_path)
        result["output_raw"] = str(raw_path)
        log(f"    Generiert in {gen_time:.1f}s (Seed: {result['seed']})")

    except requests.Timeout:
        result["error"] = "Timeout (>300s)"
        result["time_generate"] = 300
        log(f"    TIMEOUT!")
        return result
    except Exception as e:
        result["error"] = str(e)
        log(f"    FEHLER: {e}")
        traceback.print_exc()
        return result

    # 2. Hintergrund entfernen
    start_bg = time.time()
    try:
        img_nobg = process_with_rembg(img)
        bg_time = time.time() - start_bg
        result["time_rembg"] = round(bg_time, 1)

        nobg_path = out_dir / f"elise_{expression}_nobg.png"
        img_nobg.save(nobg_path)
        result["output_nobg"] = str(nobg_path)
        log(f"    rembg in {bg_time:.1f}s")

    except Exception as e:
        result["error"] = f"rembg Fehler: {e}"
        log(f"    rembg FEHLER: {e}")
        img_nobg = img.convert("RGBA")

    # 3. Sprite zuschneiden
    try:
        sprite = crop_to_sprite(img_nobg)
        final_path = out_dir / f"elise_{expression}.png"
        sprite.save(final_path)
        result["output_final"] = str(final_path)
        result["success"] = True
        log(f"    -> {final_path.name} (600x900)")
    except Exception as e:
        result["error"] = f"Crop Fehler: {e}"
        log(f"    Crop FEHLER: {e}")

    return result


# ============================================================================
# Hauptlogik
# ============================================================================

def run_config(config_name: str, config: dict, expressions: list[str]) -> list[dict]:
    """Fuehre alle Tests fuer eine Konfiguration durch."""
    log(f"\n{'='*70}")
    log(f"Config: {config_name}")
    log(f"  {config['description']}")
    log(f"  Modell: {config['model_search']}")
    log(f"  Sampler: {config['sampler']}, Steps: {config['steps']}, CFG: {config['cfg']}")
    log(f"  Aufloesung: {config['width']}x{config['height']}")
    log(f"{'='*70}")

    # Modell wechseln
    if not switch_model(config["model_search"]):
        log(f"  UEBERSPRUNGEN: Modell nicht verfuegbar")
        return []

    results = []
    for expr in expressions:
        result = generate_single(config_name, config, expr)
        results.append(result)
        time.sleep(2)

    return results


def write_summary(all_results: list[dict]):
    """Schreibe Zusammenfassung."""
    log(f"\n\n{'#'*70}")
    log(f"# ZUSAMMENFASSUNG")
    log(f"{'#'*70}\n")
    log(f"| Config | Expression | Erfolg | Gen (s) | rembg (s) | Seed |")
    log(f"|--------|-----------|--------|---------|-----------|------|")

    for r in all_results:
        success = "OK" if r["success"] else "FAIL"
        log(f"| {r['config']} | {r['expression']} | {success} | "
            f"{r['time_generate']} | {r['time_rembg']} | {r['seed']} |")

    log(f"\n### Ergebnisse pro Konfiguration\n")
    configs_seen = []
    for r in all_results:
        if r["config"] not in configs_seen:
            configs_seen.append(r["config"])

    for cfg in configs_seen:
        cfg_results = [r for r in all_results if r["config"] == cfg]
        ok = sum(1 for r in cfg_results if r["success"])
        total = len(cfg_results)
        avg_gen = sum(r["time_generate"] for r in cfg_results) / max(total, 1)
        avg_bg = sum(r["time_rembg"] for r in cfg_results) / max(total, 1)
        desc = cfg_results[0]["description"] if cfg_results else ""
        log(f"- **{cfg}**: {ok}/{total} OK, avg gen {avg_gen:.1f}s, avg rembg {avg_bg:.1f}s")
        log(f"  {desc}")

    log(f"\n### Dateien\n")
    log(f"Alle Testbilder in: `{TEST_DIR}`")
    log(f"Pro Config-Ordner: `elise_<expr>_raw.png` (original), "
        f"`elise_<expr>_nobg.png` (transparent), `elise_<expr>.png` (600x900 Sprite)")


def main():
    parser = argparse.ArgumentParser(description="Sprite Generation Test Suite v2")
    parser.add_argument("--configs", nargs="*", default=None,
                        help="Bestimmte Configs testen (z.B. 01_animagine_oil)")
    parser.add_argument("--expressions", nargs="*", default=["neutral", "happy", "afraid"],
                        help="Expressions zum Testen")
    parser.add_argument("--list", action="store_true", help="Configs auflisten")
    args = parser.parse_args()

    if args.list:
        print("Verfuegbare Konfigurationen:")
        for name, cfg in CONFIGS.items():
            print(f"  {name}: {cfg['description']}")
        return

    if not check_api():
        print("FEHLER: SD WebUI API nicht erreichbar auf", SD_URL)
        sys.exit(1)

    # Modell-Refresh
    log("Aktualisiere Modell-Liste...")
    try:
        requests.post(f"{SD_URL}/sdapi/v1/refresh-checkpoints", timeout=30)
        time.sleep(2)
    except:
        pass

    # Log initialisieren
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Sprite Generation Test Log v2\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Testcharakter: Elise\n")
        f.write(f"Expressions: {', '.join(args.expressions)}\n")
        f.write(f"Transparenz: rembg (alle Configs)\n\n")

    configs_to_run = args.configs if args.configs else list(CONFIGS.keys())
    all_results = []

    for config_name in configs_to_run:
        if config_name not in CONFIGS:
            log(f"WARNUNG: Unbekannte Config '{config_name}', uebersprungen")
            continue
        results = run_config(config_name, CONFIGS[config_name], args.expressions)
        all_results.extend(results)

    write_summary(all_results)

    # JSON-Export
    json_path = TEST_DIR / "results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    log(f"\nJSON-Ergebnisse: {json_path}")


if __name__ == "__main__":
    main()
