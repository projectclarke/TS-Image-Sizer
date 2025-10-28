# 🖼️ Image Resizer — 2400×2400 on White (Windows/macOS/Linux)

A simple one-click image resizing tool.  
It batch-processes all images in the **current folder**, centres them on a **2400×2400 white canvas**, preserves aspect ratio, and saves clean high-quality JPG copies into an `output_2400` folder.

---

## 📦 Features

- ✅ Automatically resizes and centres every image in the folder  
- ✅ Scales longest side to **2400 px** (keeps proportions)  
- ✅ Adds a **white background** (useful for PNG transparency)  
- ✅ Outputs high-quality `.jpg` images (quality = 95)  
- ✅ Creates an `output_2400/` folder automatically  
- ✅ Works via **double-click on Windows** or command line on macOS/Linux  

---

## 🗂️ Repository contents

| File | Description |
|------|--------------|
| `resize_core.py` | Core Python script that does the resizing, centring, and exporting |
| `resize_to_2400.bat` | Windows helper script for double-click execution (optional) |

---

## ⚙️ Requirements

- **Python 3.8 or higher**  
- **Pillow** (Python Imaging Library fork)

### Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade Pillow
On some systems use python3 instead of python.

🚀 Quick Start
🪟 Windows (double-click)
Place resize_core.py and resize_to_2400.bat in the same folder as your images.

Double-click resize_to_2400.bat.

Processed files will appear in a new folder called output_2400/.

Optional manual method:

bat
Copy code
cd path\to\your\images
python resize_core.py
🍎 macOS / 🐧 Linux
bash
Copy code
cd /path/to/your/images
python3 resize_core.py
Outputs are saved in output_2400/.

🔍 How it Works
The script creates output_2400/ if it doesn’t exist.

It scans the folder for .jpg, .jpeg, and .png files.

For each image:

Opens the image and converts transparency to white.

Calculates the scale so the longest side becomes 2400 px.

Resizes using high-quality Lanczos filtering.

Pastes it onto a 2400×2400 white background, centred perfectly.

Saves the result as filename_2400.jpg (quality 95).

🧰 Customisation
Change target size:

python
Copy code
OUTPUT_SIZE = 2400  # change to any square size, e.g., 3000
Change background colour:

python
Copy code
bg = Image.new('RGB', (OUTPUT_SIZE, OUTPUT_SIZE), 'white')  # e.g., 'black' or '#f5f5f5'
🧩 Troubleshooting
Issue	Solution
No JPG/JPEG/PNG files found	Ensure script is in same folder as your images
ModuleNotFoundError: No module named 'PIL'	Run python -m pip install Pillow
python not recognised (Windows)	Reinstall Python and tick “Add Python to PATH”
Soft or blurry output	The script already uses Lanczos (best quality for resizing)

🧠 Why 2400×2400?
Many marketplaces and catalogues require square, high-resolution product images.
A 2400 px square canvas keeps file sizes reasonable while ensuring crisp detail for thumbnails and print layouts.

🗺️ Roadmap
CLI arguments (e.g., --size 3000, --bg "#f5f5f5")

Recursive folder support

Preserve original format (e.g., PNG→PNG if desired)

🤝 Contributing
Pull requests are welcome!
Please keep it dependency-light (only Pillow) and prioritise clarity and reliability.

📄 Licence
MIT Licence — free to use, modify, and distribute.

❤️ Credits
Built with Python and Pillow.
Tested on Windows 11 and macOS Sonoma.
