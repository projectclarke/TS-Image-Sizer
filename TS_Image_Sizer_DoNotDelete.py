import os
from PIL import Image, ImageOps

OUTPUT_SIZE = 2400
MARGIN = 200  # pixels on each side
INNER_SIZE = OUTPUT_SIZE - (MARGIN * 2)
OUTPUT_DIR = 'output_2400'
VALID_EXTS = ('.jpg', '.jpeg', '.png')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def remove_white_bg(img, threshold=240):
    """
    Converts near-white areas to transparent.
    """
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    datas = img.getdata()
    new_data = []
    for item in datas:
        r, g, b, *a = item
        alpha = a[0] if a else 255
        if r > threshold and g > threshold and b > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((r, g, b, alpha))
    img.putdata(new_data)
    return img


def crop_to_content(img, safe_border=20):
    """
    Auto-crops the image to the area that actually has content.
    Adds a small safe border (pixels) to avoid clipping edges.
    """
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Use alpha channel to find bounding box of visible pixels
    bbox = img.getbbox()
    if bbox:
        left = max(bbox[0] - safe_border, 0)
        top = max(bbox[1] - safe_border, 0)
        right = min(bbox[2] + safe_border, img.width)
        bottom = min(bbox[3] + safe_border, img.height)
        img = img.crop((left, top, right, bottom))
    return img


def process_image(path):
    try:
        with Image.open(path) as im:
            im = im.convert('RGBA')

            # 1. Remove white background
            im = remove_white_bg(im)

            # 2. Auto-crop to remove excess transparent space
            im = crop_to_content(im, safe_border=20)

            # 3. Resize proportionally within the 200px margin
            w, h = im.size
            scale = INNER_SIZE / max(w, h)
            new_w = max(1, int(round(w * scale)))
            new_h = max(1, int(round(h * scale)))
            im = im.resize((new_w, new_h), Image.LANCZOS)

            # 4. Create white background
            bg = Image.new('RGB', (OUTPUT_SIZE, OUTPUT_SIZE), 'white')

            # 5. Centre on the 2400x2400 canvas
            x = (OUTPUT_SIZE - new_w) // 2
            y = (OUTPUT_SIZE - new_h) // 2
            bg.paste(im, (x, y), im if im.mode == 'RGBA' else None)

            # 6. Save output
            base = os.path.splitext(os.path.basename(path))[0]
            out_path = os.path.join(OUTPUT_DIR, f'{base}_2400.jpg')
            bg.save(out_path, 'JPEG', quality=95)
            print(f"Processed: {path} -> {out_path}")

    except Exception as e:
        print(f"ERROR processing {path}: {e}")


def main():
    files = [f for f in os.listdir('.') if f.lower().endswith(VALID_EXTS)]
    if not files:
        print("No JPG/JPEG/PNG files found.")
        return
    for f in files:
        if f.startswith('output_2400'):
            continue
        process_image(f)

if __name__ == '__main__':
    main()
