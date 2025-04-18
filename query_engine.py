import faiss
import numpy as np
import json
from llm_local import ask_local_llm  # lokale Antwortfunktion

def answer_query(query: str, index_path: str, metadata_path: str, top_k: int = 3, print_result: bool = True) -> str:
    # FAISS-Index laden
    index = faiss.read_index(f"{index_path}.faiss")

    # Metadaten laden
    with open(f"{metadata_path}_meta.json", 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # Query lokal embedden
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vector = model.encode(query).reshape(1, -1).astype('float32')

    # Ähnliche Chunks suchen
    distances, indices = index.search(query_vector, top_k)

    # Chunks zusammenstellen
    relevant_chunks = []
    for idx in indices[0]:
        meta = metadata[idx]
        snippet = meta.get("text_snippet", "")
        relevant_chunks.append(f"(Seite {meta['page']}) {snippet}")

    if print_result:
        print("\n🔎 Relevante Chunks:")
        for i, chunk in enumerate(relevant_chunks, 1):
            print(f"{i}. {chunk}\n")

    # Prompt bauen
    prompt = (
        f"Hier sind Ausschnitte aus einem Dokument:\n\n"
        f"{chr(10).join(relevant_chunks)}\n\n"
        f"Beantworte folgende Frage nur auf Basis der obigen Informationen:\n\"{query}\""
    )

    # Lokale Antwort simulieren
    return ask_local_llm(prompt)
