from PIL import Image, ImageEnhance, ImageFilter

def apply_valencia_filter(image_path, output_path, brightness_factor=1.2, contrast_factor=1.0, saturation_factor=0.9, warmth_factor=0.6):
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

    # Apply a warm tint
    r, g, b = img.split()
    r = r.point(lambda i: i * warmth_factor)
    img = Image.merge('RGB', (r, g, b))

    # Apply a slight blur for a soft effect
    img = img.filter(ImageFilter.GaussianBlur(radius=1))

    # Save the result
    img.show()