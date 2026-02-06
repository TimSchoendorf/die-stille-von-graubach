"""
img2img Konsistenz-Test
========================
Ansatz: Ein Referenzbild (neutral) generieren, dann alle Expressions
per img2img davon ableiten. Verschiedene Denoising Strengths testen.
"""
import argparse
import base64
import io
import json
import time
from pathlib import Path

import requests
from PIL import Image

SD_URL = "http://127.0.0.1:7860"
TEST_DIR = Path(r"C:\Games\VisualNovel\test_sprites")

# ============================================================================
# Settings (V5 Gewinner-Config)
# ============================================================================

QUALITY = (
    "masterpiece, best quality, detailed face, portrait, upper body, half body, "
    "looking at viewer, muted colors, 1920s germany, oil painting style, "
    "dramatic lighting, cinematic"
)
POSE_LOCK = "front view, facing viewer, centered composition, symmetrical face"
BG_POS = ", simple background, white background, solid color background, plain white background"

COMMON_NEGATIVE = (
    "lowres, bad anatomy, bad hands, text, error, missing fingers, "
    "extra digit, fewer digits, cropped, worst quality, low quality, "
    "normal quality, jpeg artifacts, signature, watermark, username, blurry, "
    "3d render, bright neon colors"
)
BG_NEG = (
    ", dark background, black background, grey background, "
    "detailed background, side view, profile, turned away"
)

ELISE_IDENTITY = (
    "1girl, solo, 24 years old, dark brown bob hair, glasses, round glasses, "
    "brown eyes, slender, pale skin, "
    "1920s german clothing, long dark coat, high collar blouse, "
    "serious intellectual look"
)
ELISE_NEG_EXTRA = ", multiple girls, male, child, modern clothing, wings"

EXPRESSIONS = {
    "neutral": "neutral expression, calm face, composed",
    "happy": "gentle smile, warm expression, soft eyes",
    "afraid": "frightened expression, wide eyes, trembling, fearful",
    "angry": "angry expression, furrowed brows, clenched jaw, intense",
    "shocked": "shocked expression, wide eyes, open mouth, gasping",
    "sad": "sad expression, downcast eyes, melancholy, sorrow",
}

# ============================================================================

def img_to_base64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


def generate_reference(seed: int = 42) -> Image.Image:
    """Generiert das Referenzbild (neutral) per txt2img."""
    prompt = f"{QUALITY}, {ELISE_IDENTITY}, {POSE_LOCK}, {EXPRESSIONS['neutral']}{BG_POS}"
    negative = COMMON_NEGATIVE + ELISE_NEG_EXTRA + BG_NEG

    payload = {
        "prompt": prompt,
        "negative_prompt": negative,
        "steps": 28,
        "cfg_scale": 7,
        "width": 832,
        "height": 1216,
        "sampler_name": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "seed": seed,
    }

    print("Generiere Referenzbild (neutral)...")
    r = requests.post(f"{SD_URL}/sdapi/v1/txt2img", json=payload, timeout=300)
    data = r.json()
    img_data = base64.b64decode(data["images"][0])
    img = Image.open(io.BytesIO(img_data))
    print(f"  OK, Seed: {json.loads(data.get('info', '{}')).get('seed', seed)}")
    return img


def generate_expression_img2img(ref_img: Image.Image, expression: str,
                                 denoising: float, seed: int = 42) -> Image.Image:
    """Generiert eine Expression per img2img vom Referenzbild."""
    prompt = f"{QUALITY}, {ELISE_IDENTITY}, {POSE_LOCK}, {EXPRESSIONS[expression]}{BG_POS}"
    negative = COMMON_NEGATIVE + ELISE_NEG_EXTRA + BG_NEG

    payload = {
        "init_images": [img_to_base64(ref_img)],
        "prompt": prompt,
        "negative_prompt": negative,
        "steps": 28,
        "cfg_scale": 7,
        "width": 832,
        "height": 1216,
        "sampler_name": "DPM++ 2M SDE",
        "scheduler": "Karras",
        "seed": seed,
        "denoising_strength": denoising,
    }

    r = requests.post(f"{SD_URL}/sdapi/v1/img2img", json=payload, timeout=300)
    data = r.json()
    img_data = base64.b64decode(data["images"][0])
    return Image.open(io.BytesIO(img_data))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--denoising", nargs="*", type=float,
                        default=[0.25, 0.35, 0.45, 0.55])
    args = parser.parse_args()

    # API Check
    try:
        requests.get(f"{SD_URL}/sdapi/v1/sd-models", timeout=5)
    except Exception:
        print("FEHLER: API nicht erreichbar")
        return

    # Referenzbild generieren
    ref_img = generate_reference(args.seed)
    ref_dir = TEST_DIR / "img2img_ref"
    ref_dir.mkdir(parents=True, exist_ok=True)
    ref_img.save(ref_dir / "elise_reference.png")

    # Fuer jede Denoising Strength alle Expressions generieren
    expressions_to_test = ["happy", "afraid", "angry", "shocked", "sad"]

    for dns in args.denoising:
        dns_label = f"dns{int(dns*100)}"
        out_dir = TEST_DIR / f"img2img_{dns_label}"
        out_dir.mkdir(parents=True, exist_ok=True)

        # Referenz auch hier speichern fuer Vergleich
        ref_img.save(out_dir / "elise_neutral.png")

        print(f"\n=== Denoising {dns} ({dns_label}) ===")

        for expr in expressions_to_test:
            print(f"  {expr} (dns={dns})...", end=" ", flush=True)
            t0 = time.time()
            img = generate_expression_img2img(ref_img, expr, dns, args.seed)
            dt = round(time.time() - t0, 1)
            img.save(out_dir / f"elise_{expr}.png")
            print(f"OK ({dt}s)")
            time.sleep(1)

    print(f"\nFertig! Ergebnisse in {TEST_DIR}/img2img_*/")
    print(f"Referenzbild: {ref_dir}/elise_reference.png")


if __name__ == "__main__":
    main()
