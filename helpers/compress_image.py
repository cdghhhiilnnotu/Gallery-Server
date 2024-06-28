from PIL import Image

def compress_image_to_jpeg(input_image_path, output_image_path, quality=85):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Convert the image to RGB mode if it's not already in that mode
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Save the image with the specified quality level
        img.save(output_image_path, 'JPEG', quality=quality)

# Example usage:
compress_image_to_jpeg('src\images\i0000000012.png', 'src\images\i0000000012.png', quality=1)