from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import base64, io

class VintageFilter:

    def apply_vintage_filter(image_path, vintage_strength=1.5):
        image_path = image_path[len("http://127.0.0.1:8000/"):]
        print("This is the image path: ", image_path)

        img = Image.open(image_path)

        # Convert the image to numpy array for more advanced operations
        img_array = np.array(img)

        # Apply vintage effect by manipulating color channels and adding noise
        img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 0.8, 0, 255)  # Red channel
        img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 0.9, 0, 255)  # Blue channel

        # Add noise
        noise = np.random.normal(loc=0, scale=10, size=img_array.shape)
        img_array = np.clip(img_array + noise, 0, 255)

        # Convert back to Pillow Image
        vintage_img = Image.fromarray(np.uint8(img_array))

        # Enhance the vintage effect using Pillow's ImageEnhance
        enhancer = ImageEnhance.Color(vintage_img)
        vintage_img = enhancer.enhance(vintage_strength)

        # Apply a slight blur for a more aged look
        vintage_img = vintage_img.filter(ImageFilter.BLUR)

        buffered = io.BytesIO()
        vintage_img.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return processed_image_base64