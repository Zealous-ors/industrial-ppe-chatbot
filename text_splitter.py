from document_loader import load_documents


def split_documents():

    documents = load_documents()

    chunks = []

    chunk_size = 1000
    overlap = 150

    for document in documents:

        text = document["text"]
        filename = document["filename"]

        start = 0
        chunk_id = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end].strip()

            if chunk:
                chunks.append({
                    "text": chunk,
                    "filename": filename,
                    "chunk_id": chunk_id
                })

            chunk_id += 1
            start += chunk_size - overlap

    print(f"\nTotal chunks created: {len(chunks)}")

    return chunks


if __name__ == "__main__":
    split_documents()