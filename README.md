# 🖼️ Image Resizer 2400x2400

A simple yet powerful **Python + Batch** tool that automatically resizes and cleans up images for product catalogues, e-commerce listings, and marketing materials.  

It scales, centres, and cleans your images on a perfect **2400 × 2400 white background** — removing unwanted white borders and keeping a professional, consistent look across your range.

---

## 🚀 Features

✅ **Auto-resize**  
Scales each image so its **largest side fits within a 2400 × 2400 frame**, maintaining perfect aspect ratio.  

✅ **White background removal**  
Detects near-white backgrounds and makes them transparent before placing the image on a clean white canvas.  

✅ **Auto-crop to subject**  
After background removal, the script intelligently crops away any remaining empty space while keeping a small *safe zone* to avoid clipping the subject.  

✅ **Consistent margin**  
Adds a **200 px margin** around your subject, ensuring it never touches the edges of the final frame.  

✅ **Centred output**  
The image is placed precisely in the centre of a white 2400×2400 background for uniform presentation.  

✅ **Batch processing**  
Handles every `.jpg`, `.jpeg`, and `.png` in the folder automatically.

---

## 📂 Output

All processed images are saved into a sub-folder named:

output_2400/

vbnet
Copy code

Each image is renamed with a `_2400` suffix, for example:

myimage.jpg → output_2400/myimage_2400.jpg

yaml
Copy code

---

## ⚙️ Installation

1. Install [Python](https://www.python.org/downloads/) (version 3.7+ recommended).  
   During installation, tick **“Add Python to PATH”**.

2. Install Pillow (Python Imaging Library):

   ```bash
   pip install pillow
🧩 Usage
Option 1 – Double-Click Method (Windows)
Copy both files into the folder containing your images:

resize_to_2400.bat

resize_core.py

Double-click resize_to_2400.bat.

Wait until it finishes — the results will appear inside output_2400.

Option 2 – Command Line
You can also run the Python script directly:

bash
Copy code
python resize_core.py
🧠 How It Works
Scans the folder for supported image formats.

Removes white backgrounds by turning near-white pixels transparent.

Crops tightly around the subject, leaving a small safe border.

Resizes the subject to fit inside a 2200×2200 area (allowing 200 px margin).

Centres the image on a 2400×2400 white canvas.

Saves the result as a high-quality .jpg in output_2400.

🔧 Configuration
Inside resize_core.py you can adjust:

Variable	Default	Description
OUTPUT_SIZE	2400	Final canvas size (square)
MARGIN	200	Margin on each side (in pixels)
safe_border	20	Extra safe pixels when auto-cropping
threshold	240	White detection threshold (0–255)

🧪 Example Results
Input	Output
Product photo on white	Background cleaned, cropped, centred, 2400×2400
Transparent PNG	Preserved and centred with white background
Dark background photo	Scaled and centred without background removal
