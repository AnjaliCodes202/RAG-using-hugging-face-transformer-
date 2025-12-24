# from fastapi import FastAPI
# from pydantic import BaseModel
#
# from src.loader import load_file
# from src.chunker import chunk_document
# from src.embedder import Embedder
# from src.retriever import Retriever
# from src.generator import Generator
#
# app = FastAPI(title="RAG Question Answering API")
#
# # Global objects (initially empty)
# retriever = None
# generator = None
#
#
# @app.on_event("startup")
# def startup_event():
#     global retriever, generator
#
#     documents = load_file("Data/documents/")  # <-- match folder case
#     chunks = chunk_document(documents)
#
#     embedder = Embedder()
#     chunks = embedder.embed_chunks(chunks)
#
#     retriever = Retriever(chunks)
#     generator = Generator()
#
#
# # -------- SCHEMAS --------
# class QuestionRequest(BaseModel):
#     question: str
#
#
# class AnswerResponse(BaseModel):
#     answer: str
#     sources: list[str]
#
#
# # -------- ROUTE --------
# @app.post("/ask", response_model=AnswerResponse)
# def ask_question(request: QuestionRequest):
#     retrieved_chunks = retriever.retrieve(request.question, top_k=3)
#     answer = generator.generate(request.question, retrieved_chunks)
#     sources = list({chunk["filename"] for chunk in retrieved_chunks})
#
#     return {
#         "answer": answer,
#         "sources": sources
#     }

from fastapi import FastAPI
from pydantic import BaseModel

from src.loader import load_file
from src.chunker import chunk_document
from src.embedder import Embedder
from src.retriever import Retriever
from src.generator import Generator

# -----------------------------
# App initialization
# -----------------------------
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
app = FastAPI(title="RAG Question Answering API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/",
    StaticFiles(directory="Frontend", html=True),
    name="Frontend",
)

# -----------------------------
# Load pipeline ONCE (startup)
# -----------------------------
documents = load_file("data/documents/")
chunks = chunk_document(documents)

embedder = Embedder()
chunks = embedder.embed_chunks(chunks)

retriever = Retriever(chunks)
generator = Generator()

# -----------------------------
# Request / Response schema
# -----------------------------
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]

# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    retrieved_chunks = retriever.retrieve(request.question, top_k=3)
    result = generator.generate(request.question, retrieved_chunks)
    return result
