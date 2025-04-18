from pdf_parser import extract_pdf_chunks
from embed_index import index_chunks_faiss
from query_engine import answer_query

# Pfade zur PDF und zum Index-Speicherort
PDF = 'data/uploads/test.pdf'
IDX = 'data/index/companybrain_index'

# 1) PDF in Chunks aufteilen
chunks = extract_pdf_chunks(PDF)

# 2) Embeddings erzeugen und FAISS-Index speichern
index_chunks_faiss(chunks, IDX)

# 3) Beispiel-Frage stellen
antwort = answer_query(
    query="Was wurde zu Projekt X gesagt?",
    index_path=IDX,
    metadata_path=IDX
)

# 4) Ergebnis ausgeben
print("\n💬 Antwort der KI:")
print(antwort)
