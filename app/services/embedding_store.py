import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List

EMBED_DIR = "embeddings"
META_DIR = "metadata"
MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def save_embeddings_with_metadata(doc_id: str, paragraphs: List[str]):
    embeddings = MODEL.encode(paragraphs, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(EMBED_DIR, exist_ok=True)
    os.makedirs(META_DIR, exist_ok=True)

    faiss.write_index(index, f"{EMBED_DIR}/{doc_id}.faiss")

    metadata = [{"chunk_index": i, "text": p} for i, p in enumerate(paragraphs)]
    with open(f"{META_DIR}/{doc_id}_chunks.json", "w") as f:
        json.dump(metadata, f, indent=2)

def load_embeddings_and_metadata(doc_id: str):
    index = faiss.read_index(f"{EMBED_DIR}/{doc_id}.faiss")
    with open(f"{META_DIR}/{doc_id}_chunks.json") as f:
        metadata = json.load(f)
    return index, metadata
