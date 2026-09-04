from document_loader import load_documents


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def split_documents():
    """
    Split loaded documents into overlapping chunks
    while preserving source metadata.
    """

    documents = load_documents()

    chunks = []

    for document in documents:

        text = document["text"]
        filename = document["filename"]
        page = document.get("page", "Unknown")

        start = 0
        chunk_id = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end].strip()

            if chunk:
                chunks.append({
                    "text": chunk,
                    "filename": filename,
                    "page": page,
                    "chunk_id": chunk_id
                })

            chunk_id += 1
            start += CHUNK_SIZE - CHUNK_OVERLAP

    print(
        f"\nTotal chunks created: "
        f"{len(chunks)}"
    )

    return chunks


if __name__ == "__main__":
    split_documents()
