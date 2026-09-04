import chromadb

from embeddings import create_embeddings
from text_splitter import split_documents


VECTOR_DB_PATH = "vector_db"
COLLECTION_NAME = "industrial_ppe"


client = chromadb.PersistentClient(
    path=VECTOR_DB_PATH
)


def get_collection():
    """
    Get the existing ChromaDB collection.

    If the collection does not exist, create it
    from the PPE knowledge base.
    """

    try:
        return client.get_collection(
            name=COLLECTION_NAME
        )

    except ValueError:

        print(
            "Vector database not found. "
            "Creating it..."
        )

        chunks = split_documents()

        if not chunks:
            raise ValueError(
                "No documents available "
                "to create the vector database."
            )

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = create_embeddings(
            texts
        )

        collection = client.create_collection(
            name=COLLECTION_NAME
        )

        ids = [
            f"{chunk['filename']}_"
            f"{chunk.get('page', 'Unknown')}_"
            f"{chunk['chunk_id']}"
            for chunk in chunks
        ]

        metadatas = [
            {
                "filename": chunk["filename"],
                "page": chunk.get("page", "Unknown"),
                "chunk_id": chunk["chunk_id"]
            }
            for chunk in chunks
        ]

        collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(
            f"Created vector database with "
            f"{len(chunks)} chunks."
        )

        return collection


def search_documents(question, top_k=5):
    """
    Search the PPE knowledge base using
    semantic similarity.
    """

    collection = get_collection()

    query_embedding = create_embeddings(
        [question]
    )[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


if __name__ == "__main__":
    results = search_documents(
        "What PPE protects the eyes?"
    )

    print(results)
