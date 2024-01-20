from PIL import Image
import io
import base64

class GrayscaleFilter:
    def apply_grayscale_filter(image_path):

        image_path = image_path[len("http://127.0.0.1:8000/"):]
        print("This is the image path: ", image_path)

        # Open the image
        original_image = Image.open(image_path)

        # Convert the image to grayscale
        grayscale_image = original_image.convert("L")

        buffered = io.BytesIO()
        grayscale_image.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return processed_image_base64