from sentence_transformers import SentenceTransformer


# Multilingual embedding model
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


model = SentenceTransformer(MODEL_NAME)


def create_embeddings(texts):

    return model.encode(
        texts,
        normalize_embeddings=True
    ).tolist()