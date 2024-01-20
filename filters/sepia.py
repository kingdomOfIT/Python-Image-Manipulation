from PIL import Image
import numpy as np
import io, base64

class SepiaFilter:

    def apply_sepia_filter(image_path):

        image_path = image_path[len("http://127.0.0.1:8000/"):]
        print("This is the image path: ", image_path)
        
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

        buffered = io.BytesIO()
        sepia_image.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return processed_image_base64