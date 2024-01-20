from PIL import Image, ImageEnhance
import numpy as np
import io, base64

class LarkFilter:

    def apply_lark_filter(image_path):

        image_path = image_path[len("http://127.0.0.1:8000/"):]
        print("This is the image path: ", image_path)

        # Open the image using Pillow
        img = Image.open(image_path)

        # Convert the image to numpy array
        img_array = np.array(img)

        # Apply the Lark filter by manipulating the image array
        lark_filtered_array = LarkFilter.lark_filter(img_array)

        # Convert the filtered array back to an image
        lark_filtered_img = Image.fromarray(lark_filtered_array)

        buffered = io.BytesIO()
        lark_filtered_img.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return processed_image_base64


    def lark_filter(image_array):
        # Extract RGB channels
        red_channel = image_array[:,:,0]
        green_channel = image_array[:,:,1]
        blue_channel = image_array[:,:,2]

        # Apply Lark filter to each channel (you can customize this part)
        red_channel = LarkFilter.apply_channel_filter(red_channel)
        green_channel = LarkFilter.apply_channel_filter(green_channel)
        blue_channel = LarkFilter.apply_channel_filter(blue_channel)

        # Combine the filtered channels back into an image array
        filtered_array = np.stack([red_channel, green_channel, blue_channel], axis=-1)

        return filtered_array


    def apply_channel_filter(channel):
        # Customize the Lark filter for each channel (you can experiment with different filters)
        filtered_channel = channel * 1.2 + 10

        # Clip values to be within the valid range (0-255)
        filtered_channel = np.clip(filtered_channel, 0, 255)

        return filtered_channel.astype(np.uint8)