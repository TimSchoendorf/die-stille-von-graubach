"""Generate UI texture assets using Stable Diffusion or programmatically.
Run: python sd_generate_ui.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = Path(r"C:\Games\VisualNovel\assets\sprites\ui")


def create_textbox_background():
    """Create a dark semi-transparent textbox background."""
    img = Image.new("RGBA", (1920, 280), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Gradient from transparent top to dark bottom
    for y in range(280):
        alpha = int(40 + (y / 280) * 180)
        draw.line([(0, y), (1920, y)], fill=(12, 12, 20, alpha))

    # Top border line
    draw.line([(0, 0), (1920, 0)], fill=(80, 70, 60, 150), width=2)

    img.save(OUTPUT_DIR / "textbox_bg.png")
    print("  textbox_bg.png")


def create_title_background():
    """Create a dark atmospheric title screen background."""
    img = Image.new("RGB", (1920, 1080), (5, 5, 10))
    draw = ImageDraw.Draw(img)

    # Dark gradient with subtle color
    for y in range(1080):
        t = y / 1080
        r = int(5 + t * 15)
        g = int(5 + t * 10)
        b = int(10 + t * 8)
        draw.line([(0, y), (1920, y)], fill=(r, g, b))

    # Subtle fog-like circles
    fog = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    fog_draw = ImageDraw.Draw(fog)
    import random
    random.seed(42)  # Reproducible
    for _ in range(15):
        x = random.randint(0, 1920)
        y = random.randint(400, 1080)
        r = random.randint(100, 400)
        fog_draw.ellipse([x - r, y - r, x + r, y + r],
                         fill=(20, 18, 15, random.randint(5, 20)))

    fog = fog.filter(ImageFilter.GaussianBlur(50))
    img.paste(Image.alpha_composite(
        Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)), fog).convert("RGB"),
        (0, 0))

    img.save(OUTPUT_DIR / "title_bg.png")
    print("  title_bg.png")


def create_vignette_overlay():
    """Create a vignette overlay texture."""
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))

    cx, cy = 960, 540
    max_dist = math.sqrt(cx ** 2 + cy ** 2)

    for y in range(1080):
        for x in range(0, 1920, 4):  # Step by 4 for performance
            dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            t = dist / max_dist
            alpha = int(max(0, min(255, (t - 0.4) * 400)))
            for dx in range(4):
                if x + dx < 1920:
                    img.putpixel((x + dx, y), (0, 0, 0, alpha))

    img.save(OUTPUT_DIR / "vignette.png")
    print("  vignette.png")


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Generating UI textures...")
    create_textbox_background()
    create_title_background()
    create_vignette_overlay()
    print("Done!")
