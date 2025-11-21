import pdfplumber
import pytesseract
from PIL import Image
import os

# 🔹 Ruta al ejecutable de Tesseract (IMPORTANTE)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extraer_texto_pdf(path):
    texto = ""
    with pdfplumber.open(path) as pdf:
        for pagina in pdf.pages:
            contenido = pagina.extract_text()
            if contenido:
                texto += contenido + "\n"
    return texto

def extraer_texto_imagen(path):
    imagen = Image.open(path)
    texto = pytesseract.image_to_string(imagen)
    return texto.strip()

