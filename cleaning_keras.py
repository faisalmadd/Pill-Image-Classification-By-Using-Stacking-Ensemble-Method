import os
import tensorflow as tf
from PIL import Image
import numpy as np

# Define folder path
folder_path = './Pill Dataset'

# Get all subfolders in the folder
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

# Loop through each subfolder
for subfolder in subfolders:
    class_images = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(('.png', '.jpg', '.jpeg'))]

    # For each image in the subfolder
    for image_path in class_images:
        # Check file size
        if os.path.getsize(image_path) > 0:
            img = Image.open(image_path)
            # Check image size
            if img.size != (300, 300):
                img = img.resize((300, 300))
        else:
            print(f"Ignoring {image_path} as its file size is 0KB.")