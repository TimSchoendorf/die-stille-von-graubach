"""Generate character sprites using Stable Diffusion WebUI Forge API.
Uses Animagine XL 3.1 model. Run: python sd_generate_characters.py [character|all]
"""
import argparse
import base64
import io
import json
import os
import sys
import time
from pathlib import Path

import requests
from PIL import Image

SD_URL = "http://127.0.0.1:7860"
OUTPUT_DIR = Path(r"C:\Games\VisualNovel\assets\sprites\characters")

# Fixed identity prompts per character - only expression varies
CHARACTER_PROMPTS = {
    "elise": {
        "identity": "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
                     "brown eyes, slender, pale skin, 1920s german clothing, long dark coat, "
                     "high collar blouse, serious intellectual look",
        "negative": "multiple girls, male, child, modern clothing, fantasy armor, wings, "
                     "bright colors, anime style, chibi, deformed, bad anatomy",
        "expressions": {
            "neutral": "neutral expression, calm face",
            "happy": "gentle smile, warm expression",
            "sad": "sad expression, downcast eyes, melancholy",
            "afraid": "frightened expression, wide eyes, trembling",
            "angry": "angry expression, furrowed brows, clenched jaw",
            "shocked": "shocked expression, wide eyes, open mouth, gasping",
            "thinking": "thoughtful expression, hand on chin, contemplative",
            "determined": "determined expression, firm gaze, resolute",
            "worried": "worried expression, anxious eyes, slight frown",
        },
    },
    "voss": {
        "identity": "1man, solo, 55 years old, gaunt face, hollow cheeks, thin gray hair, "
                     "deep set dark eyes, bags under eyes, black pastor robes, white collar, "
                     "lutheran pastor, emaciated, haunted look, wrinkled skin",
        "negative": "woman, child, young, muscular, fat, modern clothing, fantasy, anime, chibi",
        "expressions": {
            "neutral": "neutral expression, weary eyes",
            "worried": "worried expression, furrowed brow, haunted look",
            "angry": "angry expression, righteous fury, intense eyes",
            "afraid": "terrified expression, pale face, shaking",
            "praying": "praying, hands clasped, eyes closed, desperate prayer",
            "broken": "broken expression, hollow eyes, defeated, tears",
            "warning": "warning expression, pointing finger, urgent look",
        },
    },
    "konrad": {
        "identity": "1man, solo, 30 years old, handsome face, warm brown eyes, wavy dark hair, "
                     "charming smile, teacher clothing 1920s, vest, rolled up sleeves, "
                     "fit build, friendly appearance",
        "negative": "woman, child, old, fat, modern clothing, fantasy, anime, chibi",
        "expressions": {
            "neutral": "neutral expression, pleasant face",
            "charming": "charming smile, warm inviting eyes, charismatic",
            "suspicious": "suspicious look, narrowed eyes, slight smirk",
            "dark": "dark expression, shadow over face, sinister undertone, eerie eyes",
            "possessed": "possessed look, glowing eyes, unnatural smile, dark aura",
            "sad": "sad expression, genuine sorrow, downcast",
            "smiling": "gentle smile, kind eyes, reassuring",
        },
    },
    "hilde": {
        "identity": "1woman, solo, 68 years old, elderly, white braided hair, weathered face, "
                     "green eyes, wise look, herbalist clothing, apron, dried herbs, "
                     "sturdy build, earth tones, wrinkled hands",
        "negative": "man, child, young, modern clothing, fantasy robes, anime, chibi",
        "expressions": {
            "neutral": "neutral expression, observant eyes",
            "wise": "wise expression, knowing look, gentle smile",
            "warning": "warning expression, serious eyes, raised hand",
            "kind": "kind expression, warm smile, gentle eyes",
            "mysterious": "mysterious expression, enigmatic smile, knowing look",
            "ritual": "ritual preparation, focused expression, herbs in hand",
            "angry": "angry expression, fierce protective look",
        },
    },
    "georg": {
        "identity": "1man, solo, 45 years old, strong build, blacksmith, dark hair graying, "
                     "weathered skin, calloused hands, simple work clothing, leather apron, "
                     "broad shoulders, tired eyes, moustache",
        "negative": "woman, child, young, modern clothing, fantasy, anime, chibi, slim",
        "expressions": {
            "neutral": "neutral expression, stoic face",
            "guilty": "guilty expression, avoiding eye contact, shame",
            "angry": "angry expression, clenched fists, protective fury",
            "sad": "sad expression, mournful eyes, heavy heart",
            "determined": "determined expression, set jaw, resolute stance",
            "afraid": "afraid expression, unusual fear in strong man, trembling",
            "protective": "protective stance, shielding gesture, fierce look",
        },
    },
    "anna": {
        "identity": "1girl, solo, 19 years old, pale blonde hair, very pale skin, light blue eyes, "
                     "ethereal appearance, thin, simple white dress, distant look, "
                     "dark circles under eyes, otherworldly beauty",
        "negative": "man, child, old, modern clothing, fantasy armor, anime, chibi, tan skin",
        "expressions": {
            "neutral": "neutral expression, distant gaze, slightly unfocused",
            "dreamy": "dreamy expression, faraway look, slight smile",
            "afraid": "afraid expression, wide frightened eyes, clutching arms",
            "drawing": "drawing expression, focused on paper, spiral patterns",
            "possessed": "possessed look, blank eyes, unnatural stillness, eerie",
            "lucid": "lucid moment, clear eyes, urgent expression, aware",
            "crying": "crying, tears streaming, overwhelmed",
        },
    },
    "otto": {
        "identity": "1man, solo, 60 years old, heavy set, gray hair slicked back, "
                     "thick moustache, ruddy face, mayor clothing 1920s, formal suit, "
                     "pocket watch, authoritative stance, imposing presence",
        "negative": "woman, child, young, slim, modern clothing, fantasy, anime, chibi",
        "expressions": {
            "neutral": "neutral expression, calculating eyes",
            "authoritative": "authoritative expression, commanding presence",
            "threatening": "threatening expression, cold eyes, veiled menace",
            "jovial": "jovial expression, hearty laugh, red cheeks",
            "angry": "angry expression, red face, shouting",
            "desperate": "desperate expression, wild eyes, losing control",
        },
    },
    "margarethe": {
        "identity": "1woman, solo, 78 years old, very elderly, white thin hair in bun, "
                     "deeply wrinkled face, kind but knowing eyes, dark shawl, "
                     "traditional german grandmother clothing, frail frame",
        "negative": "man, child, young, modern clothing, fantasy, anime, chibi",
        "expressions": {
            "neutral": "neutral expression, gentle face",
            "kind": "kind expression, warm grandmother smile",
            "warning": "warning expression, urgent eyes, grasping gesture",
            "young": "younger version, 40 years old, same features but less wrinkled, dark hair",
            "ghostly": "ghostly appearance, transparent, ethereal glow, spirit form",
        },
    },
}

COMMON_QUALITY = "masterpiece, best quality, detailed face, portrait, upper body, half body, " \
                 "looking at viewer, dark atmosphere, muted colors, 1920s germany, " \
                 "oil painting style, dramatic lighting"

COMMON_NEGATIVE = "lowres, bad anatomy, bad hands, text, error, missing fingers, " \
                  "extra digit, fewer digits, cropped, worst quality, low quality, " \
                  "normal quality, jpeg artifacts, signature, watermark, username, blurry, " \
                  "3d render, cartoon, bright neon colors"


def check_sd_api():
    """Check if SD WebUI API is available."""
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5)
        return r.status_code == 200
    except requests.ConnectionError:
        return False


def set_model(model_name: str = "animagine"):
    """Switch to the appropriate model."""
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=10)
        models = r.json()
        for m in models:
            if model_name.lower() in m["model_name"].lower():
                requests.post(f"{SD_URL}/sdapi/v1/options",
                              json={"sd_model_checkpoint": m["title"]}, timeout=60)
                print(f"Switched to model: {m['title']}")
                return True
        print(f"Model '{model_name}' not found. Available: {[m['model_name'] for m in models]}")
        return False
    except Exception as e:
        print(f"Error setting model: {e}")
        return False


def generate_sprite(char_id: str, expression: str, prompt_data: dict) -> bool:
    """Generate a single character sprite."""
    identity = prompt_data["identity"]
    expr_prompt = prompt_data["expressions"][expression]
    char_negative = prompt_data.get("negative", "")

    full_prompt = f"{COMMON_QUALITY}, {identity}, {expr_prompt}, simple background, white background"
    full_negative = f"{COMMON_NEGATIVE}, {char_negative}"

    payload = {
        "prompt": full_prompt,
        "negative_prompt": full_negative,
        "steps": 28,
        "cfg_scale": 7,
        "width": 1024,
        "height": 1024,
        "sampler_name": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "batch_size": 1,
        "n_iter": 1,
    }

    try:
        r = requests.post(f"{SD_URL}/sdapi/v1/txt2img", json=payload, timeout=120)
        if r.status_code != 200:
            print(f"  ERROR: API returned {r.status_code}")
            return False

        data = r.json()
        img_data = base64.b64decode(data["images"][0])
        img = Image.open(io.BytesIO(img_data))

        # Save full image for reference
        out_dir = OUTPUT_DIR / char_id
        out_dir.mkdir(parents=True, exist_ok=True)

        # Save raw
        raw_path = out_dir / f"{expression}_raw.png"
        img.save(raw_path)

        # Process: remove background, crop to 600x900
        processed = process_sprite(img)
        final_path = out_dir / f"{expression}.png"
        processed.save(final_path)

        print(f"  Generated: {char_id}/{expression}.png")
        return True

    except requests.Timeout:
        print(f"  TIMEOUT generating {char_id}/{expression}")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def process_sprite(img: Image.Image) -> Image.Image:
    """Remove background and crop to 600x900."""
    try:
        from rembg import remove
        # Remove background
        img_no_bg = remove(img)
    except ImportError:
        print("  Warning: rembg not available, keeping background")
        img_no_bg = img.convert("RGBA")

    # Crop to upper body (top 75% of image, centered)
    w, h = img_no_bg.size
    crop_h = int(h * 0.85)
    margin = int(w * 0.1)
    cropped = img_no_bg.crop((margin, 0, w - margin, crop_h))

    # Resize to 600x900
    result = cropped.resize((600, 900), Image.Resampling.LANCZOS)
    return result


def generate_character(char_id: str):
    """Generate all expressions for a character."""
    if char_id not in CHARACTER_PROMPTS:
        print(f"Unknown character: {char_id}")
        print(f"Available: {', '.join(CHARACTER_PROMPTS.keys())}")
        return

    data = CHARACTER_PROMPTS[char_id]
    print(f"\nGenerating {char_id} ({len(data['expressions'])} expressions)...")

    for expr in data["expressions"]:
        generate_sprite(char_id, expr, data)
        time.sleep(1)  # Brief pause between generations


def generate_all():
    """Generate sprites for all characters."""
    for char_id in CHARACTER_PROMPTS:
        generate_character(char_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate character sprites via SD WebUI API")
    parser.add_argument("target", nargs="?", default="all",
                        help="Character ID or 'all'")
    parser.add_argument("--no-model-switch", action="store_true",
                        help="Skip model switching")
    args = parser.parse_args()

    if not check_sd_api():
        print("ERROR: SD WebUI API not available at", SD_URL)
        print("Start Stable Diffusion WebUI Forge first.")
        sys.exit(1)

    if not args.no_model_switch:
        if not set_model("animagine"):
            print("WARNING: Could not switch to Animagine XL model")

    if args.target == "all":
        generate_all()
    else:
        generate_character(args.target)

    print("\nDone!")
