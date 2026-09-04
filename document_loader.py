import os
from pypdf import PdfReader


DOCUMENTS_FOLDER = "documents"


def load_documents():
    """
    Load PDF documents from the knowledge base.

    Each PDF page is stored separately so that
    page-level source information can be preserved
    throughout the RAG pipeline.
    """

    documents = []

    if not os.path.exists(DOCUMENTS_FOLDER):
        print(
            f"Documents folder not found: "
            f"{DOCUMENTS_FOLDER}"
        )
        return documents

    for filename in sorted(
        os.listdir(DOCUMENTS_FOLDER)
    ):

        if not filename.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(
            DOCUMENTS_FOLDER,
            filename
        )

        try:
            reader = PdfReader(file_path)

            for page_number, page in enumerate(
                reader.pages,
                start=1
            ):
                page_text = page.extract_text()

                if not page_text or not page_text.strip():
                    continue

                documents.append({
                    "filename": filename,
                    "page": page_number,
                    "text": page_text.strip()
                })

            print(
                f"Loaded: {filename} "
                f"({len(reader.pages)} pages)"
            )

        except Exception as e:
            print(
                f"Error loading {filename}: {e}"
            )

    print(
        f"\nTotal pages loaded: "
        f"{len(documents)}"
    )

    return documents


if __name__ == "__main__":
    load_documents()
