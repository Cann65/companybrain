from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import pickle
from tqdm import tqdm

def index_chunks_faiss(chunks, output_path, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = []
    metadata = []

    for chunk in tqdm(chunks, desc="Embedding chunks"):
        emb = model.encode(chunk["text"])
        embeddings.append(emb)
        metadata.append({
            "page": chunk["page"],
            "chunk_id": chunk["chunk_id"],
            "token_count": chunk["token_count"],
            "text_snippet": chunk["text"][:100]
        })

    matrix = np.array(embeddings, dtype="float32")
    dim = matrix.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(matrix)

    faiss.write_index(index, f"{output_path}.faiss")

    with open(f"{output_path}_meta.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    with open(f"{output_path}_meta.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("✅ Lokale Embeddings erstellt & Index gespeichert")
    return index
