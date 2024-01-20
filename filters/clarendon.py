from PIL import Image, ImageEnhance
import numpy as np
import io
import base64

class ClarendonFilter:

    def apply_clarendon_filter(image_path):

        image_path = image_path[len("http://127.0.0.1:8000/"):]
        print("This is the image path: ", image_path)

        # Open the image using Pillow
        img = Image.open(image_path)

        # Convert the image to a numpy array
        img_array = np.array(img)

        # Apply Clarendon filter adjustments
        img_array = ClarendonFilter.increase_contrast(img_array)
        img_array = ClarendonFilter.increase_saturation(img_array)
        img_array = ClarendonFilter.adjust_colors(img_array)

        # Convert the numpy array back to a Pillow image
        filtered_img = Image.fromarray(img_array)

        buffered = io.BytesIO()
        filtered_img.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return processed_image_base64

    def increase_contrast(img_array, factor=1.5):
        # Increase contrast using ImageEnhance
        img = Image.fromarray(img_array)
        enhancer = ImageEnhance.Contrast(img)
        img_array_contrast = np.array(enhancer.enhance(factor))
        return img_array_contrast


    def increase_saturation(img_array, factor=1.5):
        # Increase saturation using ImageEnhance
        img = Image.fromarray(img_array)
        enhancer = ImageEnhance.Color(img)
        img_array_saturation = np.array(enhancer.enhance(factor))
        return img_array_saturation

    def adjust_colors(img_array, red_factor=1.2, green_factor=0.8, blue_factor=0.8):
        # Adjust individual color channels
        img_array[:, :, 0] = np.clip(img_array[:, :, 0] * red_factor, 0, 255)
        img_array[:, :, 1] = np.clip(img_array[:, :, 1] * green_factor, 0, 255)
        img_array[:, :, 2] = np.clip(img_array[:, :, 2] * blue_factor, 0, 255)
        return img_array