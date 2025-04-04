from fastapi import APIRouter, Query
from app.services.redactor import redact_text
from app.services.embedding_store import load_embeddings_and_metadata
from app.services.feedback_tracker import record_feedback

router = APIRouter()

@router.get("/redact")
def redact_chunk(
    doc_id: str = Query(...),
    chunk_index: int = Query(...)
):
    _, metadata = load_embeddings_and_metadata(doc_id)
    chunk = metadata[chunk_index]["text"]
    result = redact_text(chunk)
    return {
        "chunk_index": chunk_index,
        "original": chunk,
        "redacted": result["redacted_text"],
        "entities": result["entities"]
    }

@router.post("/feedback")
def submit_feedback(
    doc_id: str,
    chunk_index: int,
    approved: bool,
    comment: str = "",
):
    _, metadata = load_embeddings_and_metadata(doc_id)
    chunk = metadata[chunk_index]["text"]
    result = redact_text(chunk)
    record_feedback(
        doc_id=doc_id,
        chunk_index=chunk_index,
        original=chunk,
        redacted=result["redacted_text"],
        approved=approved,
        comment=comment,
    )
    return {"status": "feedback recorded"}
