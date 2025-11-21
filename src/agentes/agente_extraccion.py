from src import extraccion
import os

def extraer(nombre_archivo):
    ruta = os.path.join("data", nombre_archivo)

    if nombre_archivo.lower().endswith(".pdf"):
        return extraccion.extraer_texto_pdf(ruta)
    else:
        return extraccion.extraer_texto_imagen(ruta)

