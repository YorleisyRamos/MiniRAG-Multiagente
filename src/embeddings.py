import os
from dotenv import load_dotenv
import google.generativeai as genai
from tenacity import retry, wait_exponential, stop_after_attempt
import time

# Cargar API Key desde .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configurar Gemini
genai.configure(api_key=api_key)

# Función para generar embeddings desde chunks
@retry(wait=wait_exponential(min=1, max=8), stop=stop_after_attempt(5))
def generar_embeddings(chunks):
    vectores = []

    for chunk in chunks:
        try:
            # Generar embedding con Gemini (versión 0.8.5)
            resultado = genai.embed_content(
                model="models/text-embedding-004",
                content=chunk
            )
            vector = resultado.embedding   # acceso correcto al vector
            vectores.append(vector)

            time.sleep(0.05)  # Pausa suave
        except Exception as e:
            print(f"Error generando embedding con Gemini: {e}")
            vectores.append([0] * 768)  # Gemini produce vectores de 768 dimensiones

    return vectores



