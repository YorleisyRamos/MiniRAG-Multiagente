# 🧠 Mini RAG Multiagente
**Autores:** Celena Perea, Yorleisy Ramos, Juan Esteban Ortiz  
**Fecha:** 2025-11-18  
**Curso:** Inteligencia Artificial.  

---

## 📄 Resumen Ejecutivo
Este proyecto implementa un sistema de **Recuperación Aumentada con Generación (RAG)** usando una arquitectura **multiagente**.  
Permite cargar documentos PDF o imágenes, extraer texto, dividirlo en fragmentos, generar embeddings con **Gemini**, comparar similitudes y responder preguntas en un chat interactivo.

---

## 🎯 Objetivos
- **General:** Crear un asistente capaz de responder preguntas basadas en documentos cargados.  
- **Específicos:**  
  - Implementar agentes para extracción, análisis y respuesta.  
  - Usar embeddings de Gemini para representación semántica.  
  - Integrar similitud con `cosine_similarity`.  
  - Diseñar interfaz en Streamlit con estilo de chat.  


---

## ⚙️ Arquitectura del Sistema

El sistema está compuesto por cinco fases principales:

Carga del archivo (PDF o imagen).
Extracción de texto mediante OCR y lectura directa de PDF.
División del texto en fragmentos o chunks.
Generación de embeddings usando Gemini.
Búsqueda de similitud y respuesta a través del chat.
A continuación se presenta el diagrama general:

flowchart TD
    A[Documento PDF/Imagen] --> B[Extracción de texto]
    B --> C[Chunking del contenido]
    C --> D[Generación de embeddings con Gemini]
    D --> E[Cálculo de similitud de consulta]
    E --> F[Respuesta generada en el chat]



| Componente          | Tecnología / Librería              |
| ------------------- | ---------------------------------- |
| Extracción de texto | pdfplumber, pytesseract, Pillow    |
| Chunking            | Funciones personalizadas en Python |
| Embeddings          | Gemini (google-generativeai)       |
| Similitud semántica | cosine_similarity (scikit-learn)   |
| Interfaz            | Streamlit + HTML/CSS personalizado |
| Manejo de API Keys  | python-dotenv                      |
| Reintentos          | tenacity                           |

Librerías Requeridas
streamlit
google-generativeai
scikit-learn
python-dotenv
tenacity
pdfplumber
pytesseract
Pillow

. Instalar dependencias

Si existe un archivo requirements.txt:
pip install -r requirements.txt

Si no existe:
pip install streamlit google-generativeai scikit-learn python-dotenv tenacity pdfplumber pytesseract Pillow














venv\Scripts\activate


$env:PYTHONPATH = (Get-Location)

streamlit run src/app.py