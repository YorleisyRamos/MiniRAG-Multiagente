import os
from dotenv import load_dotenv
import google.generativeai as genai
from tenacity import retry, wait_exponential, stop_after_attempt

# Cargar API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(5))
def procesar(chunks):
    """
    Procesa los chunks de texto y devuelve sus embeddings usando Gemini.
    """
    vectores = []
    for texto in chunks:
        try:
            emb = genai.embed_content(
                model="models/text-embedding-004",
                content=texto
            )
            vectores.append(emb["embedding"])  # ✅ dict access
        except Exception as e:
            print(f"Error generando embedding con Gemini: {e}")
            vectores.append([0] * 768)  # Gemini produce vectores de 768 dimensiones
    return vectores






