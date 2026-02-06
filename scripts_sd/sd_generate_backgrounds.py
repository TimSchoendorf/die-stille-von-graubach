"""Generate background images using Stable Diffusion WebUI Forge API.
Uses juggernautXL model. Run: python sd_generate_backgrounds.py [name|all]
"""
import argparse
import base64
import io
import os
import sys
import time
from pathlib import Path

import requests
from PIL import Image

SD_URL = "http://127.0.0.1:7860"
OUTPUT_DIR = Path(r"C:\Games\VisualNovel\assets\sprites\backgrounds")

BACKGROUND_PROMPTS = {
    # Prologue
    "berlin_apartment": {
        "prompt": "interior of small 1920s german apartment, cluttered desk with books, "
                  "rain on window, warm dim lamp light, papers scattered, typewriter, "
                  "wooden furniture, cozy but cramped, autumn evening",
        "time": "evening",
    },
    "train_interior": {
        "prompt": "interior of 1920s european train compartment, wooden seats, "
                  "window showing passing dark forest, dim compartment lighting, "
                  "leather luggage, vintage atmosphere, lonely journey",
        "time": "day",
    },
    "village_entrance": {
        "prompt": "entrance to small german black forest village 1920s, fog between "
                  "half-timbered houses, cobblestone path, bare autumn trees, "
                  "no people, eerie silence, overcast sky, dusk",
        "time": "dusk",
    },
    # Act 1
    "grandmother_house": {
        "prompt": "interior of old german cottage, death bed with white sheets, "
                  "burning candle on nightstand, dried herbs hanging, lace curtains, "
                  "dark wood furniture, somber atmosphere, dim light",
        "time": "evening",
    },
    "village_square": {
        "prompt": "small german village square 1920s, stone fountain in center, "
                  "half-timbered houses, church steeple in background, fog, "
                  "cobblestones, deserted, autumn leaves, overcast",
        "time": "day",
    },
    "church_exterior": {
        "prompt": "old german village church exterior, gothic elements, stone walls, "
                  "bell tower, iron gate, overgrown cemetery beside it, fog, "
                  "dark clouds, ominous atmosphere, 1920s",
        "time": "day",
    },
    "church_interior": {
        "prompt": "interior of old german village church, wooden pews, altar, "
                  "stained glass windows with dim light, candles, stone floor, "
                  "dark shadows, sense of something hidden beneath",
        "time": "evening",
    },
    "blacksmith_shop": {
        "prompt": "interior of 1920s german blacksmith workshop, forge with embers, "
                  "anvil, tools on wall, iron works, warm orange glow, "
                  "dark corners, practical workspace, lived-in feel",
        "time": "day",
    },
    "hilde_cottage": {
        "prompt": "interior of herbalist cottage, dried herbs everywhere, "
                  "glass jars with mysterious contents, wooden shelves, "
                  "small fire, mortar and pestle, cat, rustic cozy, "
                  "pagan symbols subtly hidden, earthy atmosphere",
        "time": "evening",
    },
    "village_school": {
        "prompt": "interior of 1920s german village school classroom, wooden desks, "
                  "chalkboard, globe, books, simple decoration, "
                  "large windows with forest view, quiet empty room",
        "time": "day",
    },
    "forest_path": {
        "prompt": "dark black forest path, tall dense pine trees, fog between trunks, "
                  "narrow dirt path, roots crossing, dim dappled light, "
                  "mysterious deep forest, slightly oppressive atmosphere",
        "time": "day",
    },
    "forest_night": {
        "prompt": "black forest at night, moonlight through branches, dense fog, "
                  "twisted tree silhouettes, darkness between trees, "
                  "unsettling shapes in shadows, path barely visible",
        "time": "night",
    },
    # Act 2-3
    "church_basement": {
        "prompt": "hidden chamber beneath old church, stone stairs leading down, "
                  "ancient carved symbols on walls, flickering torchlight, "
                  "spiral patterns, damp stone, sense of great age and dread",
        "time": "underground",
    },
    "ritual_chamber": {
        "prompt": "underground ritual chamber, stone circle, carved floor symbols, "
                  "ancient altar, darkness beyond torchlight, impossible geometry hints, "
                  "oppressive atmosphere, spiraling patterns, dread",
        "time": "underground",
    },
    "village_night": {
        "prompt": "german village at night, half-timbered houses, all windows dark, "
                  "full moon, deep fog, empty cobblestone streets, "
                  "single distant figure, haunting atmosphere",
        "time": "night",
    },
    "grandmother_house_night": {
        "prompt": "interior of old cottage at night, moonlight through window, "
                  "shadows stretching unnaturally, candle flickering, "
                  "sense of presence, creaking wooden floor, eerie stillness",
        "time": "night",
    },
    # Corrupted variants
    "village_corrupted": {
        "prompt": "german village with reality distortion, buildings slightly wrong angles, "
                  "sky wrong color, fog with dark tendrils, spiral patterns in clouds, "
                  "empty streets, surreal nightmare version, trees too close",
        "time": "corrupted",
    },
    "forest_corrupted": {
        "prompt": "black forest with reality breaking, trees bending impossibly, "
                  "glowing spiral symbols on bark, fog with faces, "
                  "path splitting in wrong directions, cosmic horror hints",
        "time": "corrupted",
    },
    "church_corrupted": {
        "prompt": "village church interior distorted, pews twisted, stained glass "
                  "showing wrong images, floor cracking with light beneath, "
                  "altar floating slightly, reality bending, horror",
        "time": "corrupted",
    },
}

COMMON_QUALITY = "masterpiece, best quality, detailed background, no people, empty scene, " \
                 "atmospheric, cinematic composition, 1920s germany, dark atmosphere, " \
                 "muted desaturated colors, oil painting style, realistic"

COMMON_NEGATIVE = "people, person, figure, character, face, anime, cartoon, 3d render, " \
                  "bright colors, neon, modern, text, watermark, signature, " \
                  "lowres, bad quality, blurry, oversaturated"

TIME_MODIFIERS = {
    "day": "overcast daylight, gray sky, diffused light",
    "evening": "warm dim interior lighting, candlelight, golden hour remnants",
    "dusk": "twilight, orange and purple sky, fading light, long shadows",
    "night": "moonlight, dark blue tones, deep shadows, silver highlights",
    "underground": "torchlight, warm flickering light, deep shadows, stone reflections",
    "corrupted": "unnatural lighting, slightly wrong colors, eerie glow, unsettling tones",
}


def check_sd_api():
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5)
        return r.status_code == 200
    except requests.ConnectionError:
        return False


def set_model(model_name: str = "juggernaut"):
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


def generate_background(name: str) -> bool:
    if name not in BACKGROUND_PROMPTS:
        print(f"Unknown background: {name}")
        return False

    data = BACKGROUND_PROMPTS[name]
    time_mod = TIME_MODIFIERS.get(data.get("time", "day"), "")

    full_prompt = f"{COMMON_QUALITY}, {data['prompt']}, {time_mod}"

    payload = {
        "prompt": full_prompt,
        "negative_prompt": COMMON_NEGATIVE,
        "steps": 28,
        "cfg_scale": 7,
        "width": 1344,
        "height": 768,
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

        result = r.json()
        img_data = base64.b64decode(result["images"][0])
        img = Image.open(io.BytesIO(img_data))

        # Resize to 1920x1080
        img_resized = img.resize((1920, 1080), Image.Resampling.LANCZOS)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Save raw
        raw_path = OUTPUT_DIR / f"{name}_raw.png"
        img.save(raw_path)

        # Save resized
        final_path = OUTPUT_DIR / f"{name}.png"
        img_resized.save(final_path)

        print(f"  Generated: {name}.png")
        return True

    except requests.Timeout:
        print(f"  TIMEOUT generating {name}")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def generate_all():
    total = len(BACKGROUND_PROMPTS)
    for i, name in enumerate(BACKGROUND_PROMPTS, 1):
        print(f"\n[{i}/{total}] Generating {name}...")
        generate_background(name)
        time.sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate backgrounds via SD WebUI API")
    parser.add_argument("target", nargs="?", default="all",
                        help="Background name or 'all'")
    parser.add_argument("--no-model-switch", action="store_true",
                        help="Skip model switching")
    parser.add_argument("--list", action="store_true",
                        help="List available backgrounds")
    args = parser.parse_args()

    if args.list:
        print("Available backgrounds:")
        for name, data in BACKGROUND_PROMPTS.items():
            print(f"  {name} ({data.get('time', 'day')})")
        sys.exit(0)

    if not check_sd_api():
        print("ERROR: SD WebUI API not available at", SD_URL)
        print("Start Stable Diffusion WebUI Forge first.")
        sys.exit(1)

    if not args.no_model_switch:
        if not set_model("juggernaut"):
            print("WARNING: Could not switch to juggernautXL model")

    if args.target == "all":
        generate_all()
    else:
        generate_background(args.target)

    print("\nDone!")
