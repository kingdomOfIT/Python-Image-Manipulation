from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # Open the image
    original_image = Image.open(input_image_path)

    # Convert the image to grayscale
    grayscale_image = original_image.convert("L")

    # Save the grayscale image
    grayscale_image.show()