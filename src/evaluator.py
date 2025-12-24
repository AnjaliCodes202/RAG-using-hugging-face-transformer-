def inspect_retrieval(question, retrived_chunks):
    print("\n=== RETRIEVAL INSPECTION ===")
    print("question: ", question)

    for i, chunk in enumerate(retrived_chunks,1):
        print(f"\nChunk {i}")
        print("source: ",chunk["filename"])
        print("text preview:")
        print(chunk["text"][:300])