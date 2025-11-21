import os
import google.generativeai as genai
from src import similitud

def responder(pregunta, chunks, vectores, nombre_archivo=None):
    pregunta_lower = pregunta.lower()

    # Detectar si la pregunta es sobre nombre o título del archivo
    if nombre_archivo and any(k in pregunta_lower for k in ["nombre", "llama", "título", "cómo se llama"]):
        return f"📂 El nombre del archivo es: {nombre_archivo}"

    # Embedding de la pregunta
    emb = genai.embed_content(
        model="models/text-embedding-004",
        content=pregunta
    )
    vector_pregunta = emb["embedding"]

    # Buscar chunk más similar
    indice, score = similitud.buscar_similitud(vectores, vector_pregunta)
    contexto = chunks[indice]

    # Generar un resumen breve del contexto usando Gemini
    resumen = genai.generate_text(
        model="models/gemini-1.5-flash",
        prompt=f"Resume en 2-3 líneas el siguiente texto en español:\n\n{contexto}"
    ).text

    # Respuesta cordial al usuario
    respuesta_cordial = (
        f"Espero que esta información te sea útil. "
        f"Si necesitas más detalles, estaré encantado de ayudarte."
    )

    return (
        f"📄 *Resultado basado en el documento (top 3 chunks):*\n\n"
        f"{contexto}\n\n"
        f"📝 **Resumen:** {resumen}\n\n"
        f"🔍 **Similitud:** {score:.2f}\n\n"
        f"🤝 {respuesta_cordial}"
    )






