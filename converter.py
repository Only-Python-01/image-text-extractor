import pytesseract
from PIL import Image

#visit https://onlypython01.blogspot.com/2025/05/extract-text-from-image-using-python.html for full tutorial

# ✅ Set the full path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load and process image
image = Image.open("image1.png")
text = pytesseract.image_to_string(image)


print(text)
