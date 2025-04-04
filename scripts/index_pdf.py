import argparse
from app.services.document_loader import extract_sentences_from_pdf
from app.services.embedding_store import save_embeddings_with_metadata

def main(pdf_path: str, doc_id: str):
    sentences = extract_sentences_from_pdf(pdf_path)
    save_embeddings_with_metadata(doc_id, sentences)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--doc_id", required=True, help="Document ID (used for filenames)")
    args = parser.parse_args()
    main(args.pdf, args.doc_id)
