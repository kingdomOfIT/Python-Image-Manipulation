from PIL import Image, ImageEnhance, ImageFilter
import io, base64

class ValenciaFilter:

    def apply_valencia_filter(image_path, brightness_factor=1.2, contrast_factor=1.0, saturation_factor=0.9, warmth_factor=0.6):
        image_path = image_path[len("http://127.0.0.1:8000/"):]
        print("This is the image path: ", image_path)

        # Open the image
        img = Image.open(image_path)

        # Adjust brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_factor)

        # Adjust contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_factor)

        # Adjust saturation
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(saturation_factor)

        # Convert to RGB
        img = img.convert('RGB')

        # Apply a warm tint
        r, g, b = img.split()
        r = r.point(lambda i: i * warmth_factor)
        img = Image.merge('RGB', (r, g, b))

        # Apply a slight blur for a soft effect
        img = img.filter(ImageFilter.GaussianBlur(radius=1))

        # Encode image
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return processed_image_base64