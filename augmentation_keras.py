import os
import tensorflow as tf
from PIL import Image
import numpy as np

# Define folder path
folder_path = './Pill Dataset'

# Get all subfolders in the folder
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

# Create an image generator with the required transformations
datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    horizontal_flip=True,
    vertical_flip=True,
    width_shift_range=0.2,  # 20% of total width
    height_shift_range=0.2,  # 20% of total height
    rotation_range=30,  # degrees
    zoom_range=[0.8, 1.2]  # zoom range from 0.8 to 1.2
)

# Loop through each subfolder
for subfolder in subfolders:
    class_images = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(('.png', '.jpg', '.jpeg'))]

    # For each image in the subfolder
    for image_path in class_images:
        img = Image.open(image_path)
        # Convert the image to a numpy array
        x = np.array(img)
        # Reshape the image to (1, height, width, channels)
        x = x.reshape((1,) + x.shape)
        # Generate 1 new augmented image per image
        batch = next(datagen.flow(x, batch_size=1))
        augmented_img = batch[0].astype(np.uint8)
        augmented_img_pil = Image.fromarray(augmented_img)
        # Resize the augmented image to ensure output size is always 224x224
        augmented_img_pil = augmented_img_pil.resize((224, 224))
        # Save the augmented image
        augmented_img_path = os.path.join(subfolder, 'augmented_' + os.path.basename(image_path))
        augmented_img_pil.save(augmented_img_path)
        print(f'Augmented image saved at: {augmented_img_path}')

