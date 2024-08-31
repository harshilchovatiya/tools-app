from PIL import Image
import io

def compress_image(image_file, quality):
    image = Image.open(image_file)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG", quality=quality)  
    return io.BytesIO(buffered.getvalue())
