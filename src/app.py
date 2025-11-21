import streamlit as st
import src.extraccion as extraccion
import src.chunking as chunking
import src.embeddings as embeddings
import src.similitud as similitud
from src.agentes import agente_extraccion, agente_analisis, agente_respuesta
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Mini RAG Multiagente", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 Mini RAG Multiagente</h1>", unsafe_allow_html=True)

# Inicializar estado de sesión
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
if "chunks" not in st.session_state:
    st.session_state.chunks = None
if "vectores" not in st.session_state:
    st.session_state.vectores = None
if "texto" not in st.session_state:
    st.session_state.texto = None
if "archivo_nombre" not in st.session_state:
    st.session_state.archivo_nombre = None

# =============================
#   CARGA DEL DOCUMENTO
# =============================
st.markdown("### 📄 Carga tu documento")
archivo = st.file_uploader("Sube un PDF o imagen", type=["pdf", "png", "jpg", "jpeg"])

if archivo:
    os.makedirs("data", exist_ok=True)
    ruta = f"data/{archivo.name}"
    with open(ruta, "wb") as f:
        f.write(archivo.read())

    st.success("Archivo cargado correctamente ✅")

    st.session_state.archivo_nombre = archivo.name

    # Extraer texto
    texto = agente_extraccion.extraer(archivo.name)
    st.session_state.texto = texto

    # Chunking y embeddings
    st.session_state.chunks = chunking.dividir_en_chunks(texto)
    st.session_state.vectores = agente_analisis.procesar(st.session_state.chunks)

    st.markdown("### 📝 Texto extraído")
    st.write(texto[:1200] + "...")

# =============================
#   CHAT
# =============================
st.markdown("### 💬 Chat con el asistente")

pregunta = st.chat_input("Escribe tu pregunta sobre el documento...")

if pregunta and st.session_state.chunks and st.session_state.vectores:
    hora = datetime.now().strftime("%I:%M %p")
    st.session_state.mensajes.append(("Tú", pregunta, hora))
    st.session_state.mensajes.append(("typing", "...", ""))

    pregunta_lower = pregunta.strip().lower()

    # 🟦 Respuesta de cortesía
    if pregunta_lower in ["ok", "gracias", "muchas gracias", "thank you", "thanks"]:
        respuesta = "¡Con gusto! Aquí estaré si necesitas algo más 😊"

    # 🟦 Pregunta: ¿Cómo se llama el PDF?
    elif "como se llama" in pregunta_lower or "nombre del pdf" in pregunta_lower or "nombre del archivo" in pregunta_lower:
        respuesta = f"📄 El nombre del archivo es: **{st.session_state.archivo_nombre}**"

    # 🟦 Resumen del PDF
    elif "resumen" in pregunta_lower or "resume" in pregunta_lower or "haz un resumen" in pregunta_lower:
        texto = st.session_state.texto
        respuesta = agente_respuesta.resumir(texto)

    # 🟦 Respuesta normal del agente RAG
    else:
        respuesta = agente_respuesta.responder(
            pregunta,
            st.session_state.chunks,
            st.session_state.vectores,
            st.session_state.archivo_nombre
        )

    st.session_state.mensajes.pop()  # elimina el "typing"
    hora2 = datetime.now().strftime("%I:%M %p")
    st.session_state.mensajes.append(("Asistente", respuesta, hora2))

# =============================
#   ESTILO iPHONE
# =============================
st.markdown("""
<style>
.chat-container {
    background-color: #E5E5EA;
    padding: 20px;
    border-radius: 25px;
    max-height: 450px;
    overflow-y: auto;
    border: 1px solid #d3d3d3;
    margin-top: 15px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
    scroll-behavior: smooth;
}
.msg-row {
    display: flex;
    align-items: flex-end;
    margin-bottom: 12px;
}
.avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    margin: 0 8px;
}
.user-msg {
    background-color: #0B93F6;
    color: white;
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 65%;
    font-size: 16px;
    line-height: 1.35;
    border-bottom-right-radius: 4px;
    animation: pop 0.2s ease-out;
}
.bot-msg {
    background-color: #FFFFFF;
    color: black;
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 65%;
    font-size: 16px;
    border-bottom-left-radius: 4px;
    animation: pop 0.2s ease-out;
    border: 1px solid #dfdfdf;
}
.typing {
    background-color: #FFFFFF;
    color: black;
    padding: 12px 16px;
    border-radius: 18px;
    border-bottom-left-radius: 4px;
    width: 60px;
    border: 1px solid #dedede;
}
.dot {
    height: 6px;
    width: 6px;
    background-color: #999;
    border-radius: 50%;
    display: inline-block;
    margin: 0 2px;
    animation: blink 1.4s infinite both;
}
@keyframes blink {
    0% { opacity: .2; }
    20% { opacity: 1; }
    100% { opacity: .2; }
}
.dot:nth-child(2) { animation-delay: 0.2s; }
.dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes pop {
    0% { transform: scale(.7); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
.hora {
    font-size: 11px;
    color: #555;
    margin-top: 2px;
}
</style>
""", unsafe_allow_html=True)

# =============================
#   CHAT HTML
# =============================
html_chat = '<div class="chat-container" id="chat-box">'

for autor, mensaje, hora in st.session_state.mensajes:
    if autor == "typing":
        html_chat += """
        <div class="msg-row">
            <img src="https://i.postimg.cc/L5y5PQB1/bot.png" class="avatar">
            <div class="typing">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>
        </div>
        """
        continue

    if autor == "Tú":
        html_chat += f"""
        <div class="msg-row" style="justify-content: flex-end;">
            <div>
                <div class="user-msg">{mensaje}</div>
                <div class="hora" style="text-align: right;">{hora}</div>
            </div>
            <img src="https://i.postimg.cc/1zgFb8mK/user.png" class="avatar">
        </div>
        """
    else:
        html_chat += f"""
        <div class="msg-row">
            <img src="https://i.postimg.cc/L5y5PQB1/bot.png" class="avatar">
            <div>
                <div class="bot-msg">{mensaje}</div>
                <div class="hora">{hora}</div>
            </div>
        </div>
        """

html_chat += """
<div id="scroll-anchor"></div>
<script>
document.getElementById('scroll-anchor').scrollIntoView();
</script>
</div>
"""

if html_chat.strip() != '<div class="chat-container" id="chat-box"></div>':
    st.markdown(html_chat, unsafe_allow_html=True)






