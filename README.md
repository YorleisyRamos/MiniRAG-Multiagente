# 🧠 Mini RAG Multiagente
**Autores:** Celena Perea, Yorleisy Ramos
**Fecha:** 2025-11-18  
**Curso:** Inteligencia Artificial  

## 📂 Estructura del Proyecto

Proyecto_MiniRAG_Multiagentes2/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .env
├── 📄 .gitignore
│
├── 📂 data/
├── 📂 docs/
├── 📂 src/
│   ├── app.py
│   ├── agentes/
│   │   ├── agente_extraccion.py
│   │   ├── agente_analisis.py
│   │   └── agente_respuesta.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── extraccion.py
│   └── similitud.py

## 🔁 Arquitectura del Sistema

```mermaid
flowchart TD
    A[📄 Documento PDF/Imagen] --> B[🔍 Extracción de texto]
    B --> C[✂️ Chunking del contenido]
    C --> D[🔑 Embeddings con Gemini]
    D --> E[📊 Similitud con la consulta]
    E --> F[💬 Respuesta generada en el chat]


---

### Instalación y Ejecución
```markdown
## 🚀 Ejecución del Proyecto

```bash
# 1. Activar el entorno virtual
venv\Scripts\activate

# 2. Establecer la variable PYTHONPATH para reconocer la carpeta src
$env:PYTHONPATH = (Get-Location)

# 3. Ejecutar la aplicación en Streamlit
streamlit run src/app.py


