

def chunk_document(document, chunk_size=300, overlap=50):
    if(chunk_size<=overlap):
        raise ValueError("chunk_size must be greater than overlap")
    chunks = []
    for docs in document:
        text = docs["text"]
        filename = docs["filename"]
        start = 0;
        doc_len = len(text);
        while start<doc_len:
            end = start+chunk_size
            chunk_text = text[start:end]
            chunks.append({
                'filename': filename,
                'text': chunk_text,
                'start': start,
                'end': end
            })
            start = end-overlap
    return chunks



   