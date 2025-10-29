@echo off
title Resize Images to 2400x2400 (Centered on White)

echo.
echo Welcome to the Toolsaver Image Sizer - Making lives easier since 2025
echo.
echo Press any key to process all images in this folder...
pause >nul

echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Install it from python.org and run this again.
    pause
    exit /b
)

echo Checking Pillow...
python -c "from PIL import Image" 2>nul
if errorlevel 1 (
    echo Installing Pillow...
    python -m pip install pillow
)

echo Running resize script...
python TS_Image_Sizer_DoNotDelete.py

echo.
echo The Toolsaver Image Sizer has Finished! New files saved in folder: output_2400
echo.
echo Press any key to close...
pause >nul
exit
