import os
from pypdf import PdfReader

DOCUMENTS_FOLDER = "documents"


def load_documents():
    documents = []

    for filename in os.listdir(DOCUMENTS_FOLDER):

        if not filename.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(DOCUMENTS_FOLDER, filename)

        try:
            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            if text.strip():
                documents.append({
                    "filename": filename,
                    "text": text
                })

                print(f"Loaded: {filename}")

        except Exception as e:
            print(f"Error loading {filename}: {e}")

    print(f"\nTotal documents loaded: {len(documents)}")

    return documents


if __name__ == "__main__":
    load_documents()