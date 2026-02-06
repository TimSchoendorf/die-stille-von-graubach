"""Generate placeholder assets for development."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Games\VisualNovel\assets\sprites"

# Character placeholders: colored silhouettes 600x900
CHARACTERS = {
    "elise": {"color": (200, 184, 150), "label": "Elise"},
    "voss": {"color": (139, 143, 163), "label": "Pfarrer Voss"},
    "konrad": {"color": (168, 144, 112), "label": "Konrad"},
    "hilde": {"color": (122, 155, 109), "label": "Hilde"},
    "georg": {"color": (176, 136, 96), "label": "Georg"},
    "anna": {"color": (155, 170, 184), "label": "Anna"},
    "otto": {"color": (139, 115, 85), "label": "Buergermeister"},
    "margarethe": {"color": (160, 144, 128), "label": "Grossmutter"},
}

EXPRESSIONS = {
    "elise": ["neutral", "happy", "sad", "afraid", "angry", "shocked", "thinking", "determined", "worried"],
    "voss": ["neutral", "worried", "angry", "afraid", "praying", "broken", "warning"],
    "konrad": ["neutral", "charming", "suspicious", "dark", "possessed", "sad", "smiling"],
    "hilde": ["neutral", "wise", "warning", "kind", "mysterious", "ritual", "angry"],
    "georg": ["neutral", "guilty", "angry", "sad", "determined", "afraid", "protective"],
    "anna": ["neutral", "dreamy", "afraid", "drawing", "possessed", "lucid", "crying"],
    "otto": ["neutral", "authoritative", "threatening", "jovial", "angry", "desperate"],
    "margarethe": ["neutral", "kind", "warning", "young", "ghostly"],
}

# Background placeholders: gradient rectangles 1920x1080
BACKGROUNDS = {
    "berlin_apartment": {"top": (60, 55, 50), "bottom": (30, 28, 25), "label": "Berlin - Wohnung"},
    "train_interior": {"top": (50, 45, 40), "bottom": (35, 30, 25), "label": "Zug - Innen"},
    "village_entrance": {"top": (40, 50, 45), "bottom": (20, 25, 20), "label": "Graubach - Eingang"},
    "grandmother_house": {"top": (45, 40, 35), "bottom": (25, 22, 18), "label": "Grossmutters Haus"},
}


def create_character_placeholder(char_id: str, expression: str, color: tuple, label: str):
    """Create a 600x900 character placeholder with silhouette shape."""
    img = Image.new("RGBA", (600, 900), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Simple silhouette shape
    r, g, b = color
    body_color = (r, g, b, 200)

    # Head (circle)
    draw.ellipse([225, 30, 375, 180], fill=body_color)
    # Neck
    draw.rectangle([275, 180, 325, 220], fill=body_color)
    # Torso
    draw.polygon([(180, 220), (420, 220), (450, 600), (150, 600)], fill=body_color)
    # Arms
    draw.polygon([(180, 240), (100, 500), (130, 510), (200, 300)], fill=body_color)
    draw.polygon([(420, 240), (500, 500), (470, 510), (400, 300)], fill=body_color)

    # Label
    try:
        font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
        small_font = font

    # Name at bottom
    text = f"{label}"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((600 - tw) // 2, 820), text, fill=(255, 255, 255, 200), font=font)

    # Expression label
    expr_text = f"[{expression}]"
    bbox2 = draw.textbbox((0, 0), expr_text, font=small_font)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((600 - tw2) // 2, 850), expr_text, fill=(200, 200, 200, 150), font=small_font)

    out_dir = os.path.join(BASE_DIR, "characters", char_id)
    os.makedirs(out_dir, exist_ok=True)
    img.save(os.path.join(out_dir, f"{expression}.png"))


def create_background_placeholder(name: str, top_color: tuple, bottom_color: tuple, label: str):
    """Create a 1920x1080 gradient background placeholder."""
    img = Image.new("RGB", (1920, 1080))
    draw = ImageDraw.Draw(img)

    for y in range(1080):
        t = y / 1080
        r = int(top_color[0] * (1 - t) + bottom_color[0] * t)
        g = int(top_color[1] * (1 - t) + bottom_color[1] * t)
        b = int(top_color[2] * (1 - t) + bottom_color[2] * t)
        draw.line([(0, y), (1920, y)], fill=(r, g, b))

    # Label
    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except OSError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((1920 - tw) // 2, (1080 - th) // 2), label,
              fill=(100, 95, 85), font=font)

    out_dir = os.path.join(BASE_DIR, "backgrounds")
    os.makedirs(out_dir, exist_ok=True)
    img.save(os.path.join(out_dir, f"{name}.png"))


def create_icon():
    """Create a simple app icon."""
    img = Image.new("RGBA", (256, 256), (10, 10, 15, 255))
    draw = ImageDraw.Draw(img)

    # Simple spiral
    import math
    cx, cy = 128, 128
    for i in range(500):
        angle = i * 0.05
        r = 5 + i * 0.15
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        if 0 <= x < 256 and 0 <= y < 256:
            alpha = max(0, 255 - i // 2)
            draw.ellipse([x-1, y-1, x+1, y+1], fill=(180, 160, 130, alpha))

    out_dir = os.path.join(BASE_DIR, "ui")
    os.makedirs(out_dir, exist_ok=True)
    img.save(os.path.join(out_dir, "icon.png"))


if __name__ == "__main__":
    print("Generating character placeholders...")
    for char_id, info in CHARACTERS.items():
        expressions = EXPRESSIONS.get(char_id, ["neutral"])
        for expr in expressions:
            create_character_placeholder(char_id, expr, info["color"], info["label"])
            print(f"  {char_id}/{expr}.png")

    print("\nGenerating background placeholders...")
    for bg_name, info in BACKGROUNDS.items():
        create_background_placeholder(bg_name, info["top"], info["bottom"], info["label"])
        print(f"  {bg_name}.png")

    print("\nGenerating icon...")
    create_icon()

    total_chars = sum(len(v) for v in EXPRESSIONS.values())
    print(f"\nDone! Generated {total_chars} character sprites, {len(BACKGROUNDS)} backgrounds, 1 icon.")
