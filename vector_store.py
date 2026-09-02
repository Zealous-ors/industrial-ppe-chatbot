import chromadb

from embeddings import create_embeddings
from text_splitter import split_documents


VECTOR_DB_PATH = "vector_db"


def create_vector_store():

    chunks = split_documents()

    texts = [chunk["text"] for chunk in chunks]

    print(f"Creating embeddings for {len(texts)} chunks...")

    embeddings = create_embeddings(texts)

    client = chromadb.PersistentClient(
        path=VECTOR_DB_PATH
    )

    collection = client.get_or_create_collection(
        name="industrial_ppe"
    )

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            {
                "filename": chunk["filename"],
                "chunk_id": chunk["chunk_id"]
            }
            for chunk in chunks
        ]
    )

    print(f"Vector database created successfully.")
    print(f"Total vectors stored: {len(chunks)}")

    return collection


if __name__ == "__main__":
    create_vector_store()