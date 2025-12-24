from src.embedder import Embedder
from src.vector_store import VectorDB
from src.vector_Store_faiss import FAISSVectorStore


class Retriever:
      def __init__(self, chunks):
           self.embedder = Embedder()
           self.vector_store = FAISSVectorStore(chunks)

      def retrieve(self, query, top_k):
          query_embedding = self.embedder.model.encode(query)
          return self.vector_store.search(query_embedding, top_k)



