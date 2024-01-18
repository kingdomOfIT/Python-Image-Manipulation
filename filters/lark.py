from PIL import Image, ImageEnhance
import numpy as np

def apply_lark_filter(image_path, output_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Convert the image to numpy array
    img_array = np.array(img)

    # Apply the Lark filter by manipulating the image array
    lark_filtered_array = lark_filter(img_array)

    # Convert the filtered array back to an image
    lark_filtered_img = Image.fromarray(lark_filtered_array)

    # Save the filtered image
    lark_filtered_img.show()


def lark_filter(image_array):
    # Extract RGB channels
    red_channel = image_array[:,:,0]
    green_channel = image_array[:,:,1]
    blue_channel = image_array[:,:,2]

    # Apply Lark filter to each channel (you can customize this part)
    red_channel = apply_channel_filter(red_channel)
    green_channel = apply_channel_filter(green_channel)
    blue_channel = apply_channel_filter(blue_channel)

    # Combine the filtered channels back into an image array
    filtered_array = np.stack([red_channel, green_channel, blue_channel], axis=-1)

    return filtered_array


def apply_channel_filter(channel):
    # Customize the Lark filter for each channel (you can experiment with different filters)
    filtered_channel = channel * 1.2 + 10

    # Clip values to be within the valid range (0-255)
    filtered_channel = np.clip(filtered_channel, 0, 255)

    return filtered_channel.astype(np.uint8)

def apply_clarendon_filter(image_path, output_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Apply Clarendon filter adjustments
    img_array = increase_contrast(img_array)
    img_array = increase_saturation(img_array)
    img_array = adjust_colors(img_array)

    # Convert the numpy array back to a Pillow image
    filtered_img = Image.fromarray(img_array)

    # Save the filtered image
    filtered_img.show()

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