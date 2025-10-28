Image Resizer — 2400×2400 on White (Windows/macOS/Linux)

A tiny utility that batch-processes images in the current folder, centres them on a 2400×2400 white canvas, preserves aspect ratio, and saves high-quality JPG copies into an output_2400 subfolder.

Supported inputs: .jpg, .jpeg, .png

Output: centred on white, scaled so the longest side becomes 2400, saved as *_2400.jpg at quality 95 in output_2400/.

Repo contents

resize_core.py — core Pillow script that does the resizing, centring, and export

resize_to_2400.bat — Windows helper for double-click execution (optional)

Prerequisites

Python 3.8+

Pillow (pip install Pillow)

Install commands
# Upgrade pip (recommended)
python -m pip install --upgrade pip

# Install Pillow
python -m pip install --upgrade Pillow


(If your system uses python3, swap python for python3.)

Quick start
Windows (double-click)

Put resize_core.py and resize_to_2400.bat in the folder that contains your images.

Double-click resize_to_2400.bat.

Processed files appear in output_2400/ with _2400.jpg suffix.

Prefer the terminal?

cd path\to\your\images
python resize_core.py

macOS / Linux (terminal)
cd /path/to/your/images
python3 resize_core.py


Outputs will be written to output_2400/.

How it works

Creates output_2400/ if it doesn’t exist.

For each JPG/PNG in the folder (ignoring the output folder itself), it:

Opens the image (handles transparency)

Computes a scale so the largest dimension becomes 2400 px, resizes with a high-quality filter

Pastes onto a white 2400×2400 background, centred

Writes *_2400.jpg (quality 95) into output_2400/

Usage details

Input formats: .jpg, .jpeg, .png in the current directory only (no subfolders)

Transparency: PNG transparency is composited onto white

Naming: originalname_2400.jpg (always JPG)

Duplicates: Re-running will overwrite files of the same name in output_2400/

Customising

Want a different box size? Edit resize_core.py:

OUTPUT_SIZE = 2400  # set your target box size here


Change the background colour (e.g., to black):

bg = Image.new('RGB', (OUTPUT_SIZE, OUTPUT_SIZE), 'white')  # change 'white'

Troubleshooting

“No JPG/JPEG/PNG files found.”
Ensure the script is in the same folder as your images and filenames end with .jpg, .jpeg or .png.

ModuleNotFoundError: No module named 'PIL'
Install Pillow in the interpreter you’re using:

python -m pip install --upgrade Pillow


Windows: python not recognised
Install Python and ensure “Add Python to PATH” is ticked, or install via Microsoft Store.

Why 2400×2400?

Square, high-resolution canvases are common for marketplaces and catalogues. 2400 px provides headroom for crisp thumbnails and moderate crops while keeping file sizes practical. The script ensures aspect-correct scaling and centred placement to avoid distortion.

Roadmap

Optional CLI flags (e.g., --size 3000, --bg "#f5f5f5", --formats .tif,.webp)

Recursive folder support

Option to preserve original format

Contributing

PRs welcome. Please keep dependencies minimal and code readable.
