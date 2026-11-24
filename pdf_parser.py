import pymupdf as fitz
import re

def extract_pdf_chunks(pdf_path: str, chunk_size: int = 500) -> list:
    doc = fitz.open(pdf_path)
    chunks = []
    chunk_id = 0

    for page_num in range(len(doc)):
        text = doc.load_page(page_num).get_text("text")

        
        if not text.strip():
            continue
        sentences = re.split(r'(?<=[.!?]) +', text)

        current_chunk = []
        current_tokens = 0

        for sent in sentences:
            tokens = sent.split()  
            n_tokens = len(tokens)

            if current_chunk and (current_tokens + n_tokens > chunk_size):
                chunks.append({
                    "text": " ".join(current_chunk),
                    "page": page_num + 1,
                    "chunk_id": chunk_id,
                    "token_count": current_tokens
                })
                chunk_id += 1
                current_chunk = []
                current_tokens = 0

            current_chunk.append(sent)
            current_tokens += n_tokens

        if current_chunk:
            chunks.append({
                "text": " ".join(current_chunk),
                "page": page_num + 1,
                "chunk_id": chunk_id,
                "token_count": current_tokens
            })
            chunk_id += 1

    return chunks
