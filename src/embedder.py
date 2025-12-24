

from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks):
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.model.encode(texts)
        for chunk,embedding in zip(chunks,embeddings):
             chunk["embedding"] = embedding
        return chunks

