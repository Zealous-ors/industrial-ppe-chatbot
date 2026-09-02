import chromadb

from embeddings import create_embeddings


VECTOR_DB_PATH = "vector_db"


client = chromadb.PersistentClient(
    path=VECTOR_DB_PATH
)

collection = client.get_collection(
    name="industrial_ppe"
)


def search_documents(question, top_k=5):

    query_embedding = create_embeddings([question])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results