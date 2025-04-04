import json
import os
from datetime import datetime

REVIEW_DIR = os.getenv("REVIEW_DIR", "reviews")

def record_feedback(doc_id: str, chunk_index: int, original: str, redacted: str, approved: bool, comment: str = ""):
    os.makedirs(REVIEW_DIR, exist_ok=True)
    review_path = f"{REVIEW_DIR}/{doc_id}_feedback.json"

    entry = {
        "timestamp": datetime.now().isoformat(),
        "chunk_index": chunk_index,
        "original": original,
        "redacted": redacted,
        "approved": approved,
        "comment": comment
    }

    if os.path.exists(review_path):
        with open(review_path, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)

    with open(review_path, "w") as f:
        json.dump(history, f, indent=2)
