import pytesseract
from PIL import Image
from io import BytesIO

def convert_image_to_text(image_file):
    # Open the image file
    image = Image.open(BytesIO(image_file.read()))
    # Perform OCR
    text = pytesseract.image_to_string(image)
    print(text)
    return text
