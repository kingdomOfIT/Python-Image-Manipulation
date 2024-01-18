from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

def apply_sepia(image_path, output_path):
    # Open the image
    original_image = Image.open(image_path)

    # Convert the image to a NumPy array
    image_array = np.array(original_image)

    # Define the Sepia filter matrix
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    # Apply the Sepia filter to the image using matrix multiplication
    sepia_image_array = np.dot(image_array[:, :, :3], sepia_filter.T).clip(0, 255).astype(np.uint8)

    # Create a new Image from the NumPy array
    sepia_image = Image.fromarray(sepia_image_array)

    # Save the sepia image
    sepia_image.show()