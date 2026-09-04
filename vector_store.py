import chromadb

from embeddings import create_embeddings
from text_splitter import split_documents


VECTOR_DB_PATH = "vector_db"
COLLECTION_NAME = "industrial_ppe"


def create_vector_store():
    """
    Create or update the ChromaDB vector store
    using the industrial PPE knowledge base.
    """

    chunks = split_documents()

    if not chunks:
        print("No documents found to index.")
        return None

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    print(
        f"Creating embeddings for "
        f"{len(texts)} chunks..."
    )

    embeddings = create_embeddings(texts)

    client = chromadb.PersistentClient(
        path=VECTOR_DB_PATH
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    collection.upsert(
        ids=[
            str(i)
            for i in range(len(chunks))
        ],
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

    print(
        "Vector database created/updated successfully."
    )

    print(
        f"Total vectors stored: "
        f"{len(chunks)}"
    )

    return collection


if __name__ == "__main__":
    create_vector_store()
