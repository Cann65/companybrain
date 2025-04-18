import streamlit as st
from pdf_parser import extract_pdf_chunks
from embed_index import index_chunks_faiss
from query_engine import answer_query
import os
import tempfile

st.set_page_config(page_title="🧠 CompanyBrain", layout="centered")
st.markdown("""
<style>
    .main {
        background-color: #f4f6fa;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.image("https://img.icons8.com/fluency/96/brain.png", width=80)
st.title("🧠 CompanyBrain")
st.caption("Dein lokaler KI-Assistent für PDF-Dokumente")
st.markdown("---")

# Upload
uploaded_file = st.file_uploader("📤 PDF hochladen:", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success("✅ PDF erfolgreich hochgeladen.")

    # Chunks extrahieren
    with st.spinner("📚 Lese und zerlege die PDF..."):
        chunks = extract_pdf_chunks(tmp_path)

    # Index erstellen
    with st.spinner("📊 Embedding & Indexierung läuft..."):
        index_path = "data/index/ui_index"
        index_chunks_faiss(chunks, index_path)

    st.success("✅ Dokument verarbeitet!")

    # Frage stellen
    st.markdown("---")
    st.subheader("💬 Frage an dein Dokument")
    user_question = st.text_input("Was möchtest du wissen?")

    if user_question:
        with st.spinner("🔎 Analysiere..."):
            answer = answer_query(user_question, index_path, index_path)
        st.markdown("### 💡 Antwort:")
        st.success(answer)

else:
    st.info("⬆️ Lade eine PDF hoch, um loszulegen.")
