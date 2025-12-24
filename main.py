# # from dotenv import load_dotenv
# # load_dotenv()
#
# from fastapi import FastAPI
# from pydantic import BaseModel
# from src.loader import load_file
# from src.chunker import chunk_document
# from src.embedder import Embedder
# from src.retriever import Retriever
# from src.generator import Generator
# from src.evaluator import inspect_retrieval
#
# # app = FastAPI(title="RAG Question Answering API")
#
# docs = load_file('data/documents/')
# # print(docs)
# chunks = chunk_document(docs)
# # print(chunks)
# # import os
# # print(repr(os.getenv("OPENAI_API_KEY")))
#
# embedder = Embedder()
# chunks = embedder.embed_chunks(chunks)
# print(len(chunks[0]["embedding"]))
# # print(chunks[0]["embedding"])
# question = "What is RAG"
#
# retriever = Retriever(chunks)
# retrived_chunks  = retriever.retrieve(question, top_k=2)
#
# # for r in results:
# #     print(r["text"])
# generator = Generator()
# result = generator.generate(question,retrived_chunks)
#
#
# # print("Answer:")
# # print(result["answer"])
#
# # print("\nSources:")
# # for src in result["sources"]:
# #     print("-", src)
#
# inspect_retrieval(question, retrived_chunks)
