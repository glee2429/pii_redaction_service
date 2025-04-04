from transformers import pipeline
from typing import List
import torch

device = 0 if torch.backends.mps.is_available() else -1
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=device)

def summarize_paragraphs(paragraphs: List[str], max_tokens: int = 512) -> str:
    text = " ".join(paragraphs[:3])[:max_tokens * 4]
    result = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return result[0]["summary_text"]
