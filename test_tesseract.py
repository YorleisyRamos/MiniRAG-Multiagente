import pytesseract

try:
    print("Ruta detectada por pytesseract:")
    print(pytesseract.pytesseract.tesseract_cmd)
    print("\nIntentando ejecutar tesseract...")
    pytesseract.get_tesseract_version()
    print("\n✔️ Python SÍ reconoce Tesseract.")
except Exception as e:
    print("\n❌ Python NO reconoce Tesseract.")
    print("Error:", e)
