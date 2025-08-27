import sys
import colorsys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple

BASE_IMAGE = "noteblock_base/noteblock_template.png"
TEXT_X = 50
TEXT_Y = 50
TEXT_BOX_WIDTH = None
FONT_PATH = "noteblock_base/font.ttf"
FONT_SIZE = 60
OUTPUT_DIR = "../noteblock"
TEXT_TEMPLATE = "{name}"
USE_STROKE = False

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_IMAGE = SCRIPT_DIR / BASE_IMAGE
FONT_PATH = SCRIPT_DIR / FONT_PATH
OUTPUT_DIR = SCRIPT_DIR / OUTPUT_DIR

NOTE_NAMES = [
    "F#3","G3","G#3","A3","A#3","B3",
    "C4","C#4","D4","D#4","E4","F4",
    "F#4","G4","G#4","A4","A#4","B4",
    "C5","C#5","D5","D#5","E5","F5","F#5"
]

def minecraft_note_rgb(index: int) -> Tuple[int, int, int]:
    """Return the RGB color for the note particle at pitch index 0..24."""
    h = index / 24.0
    r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)

def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    """Load a local TTF/OTF font file."""
    if not path.exists():
        raise FileNotFoundError(f"Font file not found: {path}")
    return ImageFont.truetype(str(path), size=size)

def draw_centered_text(draw: ImageDraw.ImageDraw, xy, text: str,
                       font: ImageFont.FreeTypeFont, fill: Tuple[int,int,int],
                       max_width: int = None, stroke_width: int = 3, stroke_fill=(0,0,0)):
    x, y = xy
    w, h = draw.textbbox((0,0), text, font=font, stroke_width=stroke_width)[2:]
    draw_x = x
    if max_width is not None:
        draw_x = x + max(0, (max_width - w) // 2)
    draw.text((draw_x, y), text, font=font, fill=fill,
              stroke_width=stroke_width, stroke_fill=stroke_fill)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    base = Image.open(BASE_IMAGE).convert("RGBA")

    try:
        font = load_font(FONT_PATH, FONT_SIZE)
    except Exception as e:
        print(f"Font error: {e}", file=sys.stderr)
        sys.exit(1)

    for idx, name in enumerate(NOTE_NAMES):
        color = minecraft_note_rgb(idx)
        label = TEXT_TEMPLATE.format(index=idx, name=name)

        im = base.copy()
        draw = ImageDraw.Draw(im)

        stroke_w = 3 if USE_STROKE else 0
        draw_centered_text(
            draw,
            (TEXT_X, TEXT_Y),
            label,
            font=font,
            fill=color,
            max_width=TEXT_BOX_WIDTH,
            stroke_width=stroke_w,
            stroke_fill=(0, 0, 0)
        )

        out_name = f"{idx}_{name.replace('#','♯')}.png"
        out_path = OUTPUT_DIR / out_name

        if out_path.exists():
            out_path.unlink()

        im.save(out_path, "PNG")
        print(f"Wrote {out_path.relative_to(SCRIPT_DIR)}")

if __name__ == "__main__":
    main()
