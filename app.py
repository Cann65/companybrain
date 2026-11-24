import streamlit as st
from pdf_parser import extract_pdf_chunks
from embed_index import index_chunks_faiss
from query_engine import answer_query
from pathlib import Path
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

st.title("🧠 CompanyBrain")
st.caption("Dein lokaler KI-Assistent für PDF-Dokumente")
st.markdown("---")

uploaded_file = st.file_uploader("PDF hochladen", type=["pdf"])
if uploaded_file is not None:
    user_question = st.text_input("Was möchtest du wissen?")
    if user_question:
        with tempfile.TemporaryDirectory() as directory:
            uploaded_pdf = Path(directory) / "document.pdf"
            uploaded_pdf.write_bytes(uploaded_file.getvalue())
            with st.spinner("Lese und zerlege die PDF…"):
                chunks = extract_pdf_chunks(str(uploaded_pdf))
            if chunks:
                with st.spinner("Suche relevante Abschnitte…"):
                    index_path = str(Path(directory) / "index")
                    index_chunks_faiss(chunks, index_path)
                    answer = answer_query(user_question, index_path, index_path)
                st.success(answer)
            else:
                st.info("Diese PDF enthält keinen extrahierbaren Text.")
else:
    st.info("Lade eine PDF hoch, um loszulegen.")
