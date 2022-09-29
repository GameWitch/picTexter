import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def ocr_read(filename, language):
    text = pytesseract.image_to_string(Image.open(filename), lang=language)
    return text
