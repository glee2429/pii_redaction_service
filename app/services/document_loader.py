import pdfplumber
import spacy
from typing import List
from loguru import logger

nlp = spacy.load("en_core_web_sm")

def extract_sentences_from_pdf(pdf_path: str, min_len: int = 20) -> List[str]:
    sentences = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                doc = nlp(text)
                for sent in doc.sents:
                    clean = sent.text.strip()
                    if len(clean) >= min_len:
                        sentences.append(clean)
    logger.info(f"Extracted {len(sentences)} sentences from {pdf_path}")
    return sentences
