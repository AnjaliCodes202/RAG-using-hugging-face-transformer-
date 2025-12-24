import faiss
import numpy as np

class FAISSVectorStore:
    def __init__(self, chunks):
        self.chunks = chunks

        self.embeddings = np.array(
            [chunk["embedding"] for chunk in chunks],
            dtype="float32"
        )

        dim = self.embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def search(self, query_embedding, top_k=3):
        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(query_embedding, top_k)

        return [self.chunks[i] for i in indices[0]]
