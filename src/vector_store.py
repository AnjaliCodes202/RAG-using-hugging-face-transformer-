import numpy as np

class VectorDB:
    def __init__(self, chunks):
        self.chunks = chunks
        self.embeddings = np.array([chunk["embedding"] for chunk in chunks])

    def cosine_similarity(self, query_embedding):
        query_embedding = np.array(query_embedding)
        dot_product = self.embeddings @ query_embedding
        norm = np.linalg.norm(self.embeddings, axis = 1) * np.linalg.norm(query_embedding)

        return dot_product/norm + 1e-10

    def search(self, query_embedding, top_k):
        similarities = self.cosine_similarity(query_embedding)
        top_indices = similarities.argsort()[-top_k:][::-1]

        return [self.chunks[i] for i in top_indices]
