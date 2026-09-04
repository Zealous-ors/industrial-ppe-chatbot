import chromadb

from embeddings import create_embeddings
from text_splitter import split_documents


VECTOR_DB_PATH = "vector_db"
COLLECTION_NAME = "industrial_ppe"


client = chromadb.PersistentClient(
    path=VECTOR_DB_PATH
)


def get_collection():

    try:

        return client.get_collection(
            name=COLLECTION_NAME
        )

    except ValueError:

        print("Vector database not found. Creating it...")

        chunks = split_documents()

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

        collection.add(
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
            f"Created vector database with "
            f"{len(chunks)} chunks."
        )

        return collection


def search_documents(question, top_k=5):

    collection = get_collection()

    query_embedding = create_embeddings(
        [question]
    )[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results
