from PIL import Image
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(SCRIPT_DIR, "redstone_base")
OUTPUT_FOLDER = os.path.join(SCRIPT_DIR, "../dust")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def shade_to_red(img, level):
    img = img.convert("RGBA")
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a > 0:
                intensity = int(80 + (level / 15) * 175)
                pixels[x, y] = (intensity, 0, 0, a)
    return img

def generate_assets():
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: Input folder not found at {INPUT_FOLDER}")
        return

    for filename in os.listdir(INPUT_FOLDER):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        asset_path = os.path.join(INPUT_FOLDER, filename)
        asset = Image.open(asset_path).convert("RGBA")
        base_name, ext = os.path.splitext(filename)

        for level in range(16):
            shaded_asset = shade_to_red(asset.copy(), level)

            output_name = f"{base_name}_SIGNAL{level}.png"
            output_path = os.path.join(OUTPUT_FOLDER, output_name)

            if os.path.exists(output_path):
                print(f"Overwriting existing file: {output_path}")
            else:
                print(f"Saving new file: {output_path}")

            shaded_asset.save(output_path)

if __name__ == "__main__":
    generate_assets()
