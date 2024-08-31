from PIL import Image
import io

def upscale_image(image_file, scale_factor):
    image = Image.open(image_file)
    width, height = image.size
    new_size = (int(width * scale_factor), int(height * scale_factor))
    resized_image = image.resize(new_size, Image.LANCZOS)
    
    buffered = io.BytesIO()
    resized_image.save(buffered, format="JPEG")
    return io.BytesIO(buffered.getvalue())
