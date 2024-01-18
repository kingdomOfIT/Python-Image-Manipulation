from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os

class Vintage:

    def apply_vintage_effect(image_path, vintage_strength=1.5):
        # Open the image using Pillow
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

        # Specify the output file path
        # name_without_extension, extenstion = os.path.splitext(os.path.basename(image_path))

        # second_file_name = f'{name_without_extension}_edited{extenstion}'


        # output_path = os.path.join("media", os.path.basename(second_file_name))
        # # Save the result
        # vintage_img.save(output_path)

        # # Return the path of the saved image
        # return output_path
    
        # Instead of saving, return the modified image as bytes
        modified_image_bytes = vintage_img.tobytes()

        return modified_image_bytes