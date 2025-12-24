# Retrieval-Augmented Generation (RAG) System — From Scratch

## Overview
This project implements an end-to-end Retrieval-Augmented Generation (RAG) system that answers user questions using external documents instead of relying solely on an LLM’s internal knowledge.

The system is designed with production principles in mind:
- modular architecture
- grounded answers
- source citations
- debuggable retrieval
- deployable API

No paid APIs are used. The system runs fully locally using open-source models.

---

## Why RAG?
Large Language Models can hallucinate or provide outdated information because they rely on static training data.

RAG solves this by:
1. Retrieving relevant document chunks using embeddings
2. Providing those chunks as context to the LLM
3. Forcing the LLM to answer only from retrieved content

This improves factual accuracy and trustworthiness.

---

## System Architecture

Documents (PDF / TXT)
-->
Document Loader
-->
Chunking (overlap)
-->
Embeddings (Sentence Transformers)
-->
Vector Similarity Search (Cosine)
-->
Relevant Chunks
-->
LLM Generator (FLAN-T5)
-->
Answer + Source Citations


---

## Core Components

### 1. Document Loader
- Supports `.txt` and `.pdf`
- Extracts clean text
- Keeps filename metadata for traceability

### 2. Chunker
- Character-based chunking
- Overlapping windows to preserve context
- Prevents context loss at boundaries

### 3. Embedder
- Uses `sentence-transformers`
- Converts text chunks into semantic vectors
- Same embedding model used for queries and documents

### 4. Vector Store & Retriever
- Implements cosine similarity from scratch
- Retrieves top-K most relevant chunks
- Fully explainable retrieval logic

### 5. Generator
- Uses open-source FLAN-T5
- Strict prompt: answers only from context
- Abstains when answer is not found
- Citations added deterministically (no hallucinated sources)

### 6. Evaluation Tools
- Retrieval inspection
- Failure mode classification
- Context visibility for debugging

### 7. FastAPI Deployment
- Pipeline loaded once at startup
- `/ask` endpoint for inference
- Swagger UI for testing

---

## API Example

### Request
```json
POST /ask
{
  "question": "What is Retrieval-Augmented Generation?"
}

{
  "answer": "Retrieval-Augmented Generation is a technique that combines information retrieval with large language models...",
  "sources": ["rag_intro.txt"]
}
