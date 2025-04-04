
# 🕵️‍♀️ PII Redaction and Human-in-the-Loop (HITL) Feedback API

This FastAPI-based system performs offline chunking + embedding of documents, then supports online redaction, summarization, and human-in-the-loop approval. It uses SpaCy for both entity-based redaction and sentence chunking, with support for custom rule-based NER via `EntityRuler`.

---

## 🚀 Features

- 🔄 **Offline chunking and embedding** using `sentence-transformers` + FAISS
- 📄 **Customizable SpaCy-based redactor** with `EntityRuler` patterns
- ⚡ **Fast online redaction API** using precomputed embeddings + metadata
- 🧠 Optional LLM-based summarization (via Hugging Face Transformers)
- 👤 **Human-in-the-loop feedback** recorded for approval workflows
- ✅ Full test suite for redaction, feedback, and route validation

---

## 🛠️ Project Structure

```
pii_redaction_service/
├── app/
│   ├── api/                  # FastAPI route handlers
│   ├── services/             # Redactor, embedding, feedback, chunking logic
│   ├── core/                 # Logging config (optional)
│   └── data/                 # Custom NER patterns (for EntityRuler)
├── embeddings/               # FAISS index files
├── metadata/                 # Chunked text for each document
├── reviews/                  # HITL feedback logs
├── sample_docs/              # Input PDFs for processing
├── scripts/
│   └── index_pdf.py          # Offline chunk + embed pipeline
├── tests/                    # Unit tests for redaction, feedback, endpoints
├── main.py                   # FastAPI app entrypoint
├── pyproject.toml            # Poetry project definition
```

---

## 🐍 Environment Setup

### Recommended: Using Poetry

```bash
poetry install
poetry run python -m spacy download en_core_web_sm
```

To activate the shell:

```bash
poetry shell
```

---

## 🧱 Offline Processing (Chunk + Embed PDF)

```bash
poetry run python scripts/index_pdf.py \
  --pdf sample_docs/your_doc.pdf \
  --doc_id=your_doc_id
```

This creates:
- `metadata/your_doc_id_chunks.json`
- `embeddings/your_doc_id.faiss`

---

## ⚡ Running the Redaction Server

```bash
poetry run uvicorn main:app --reload
```

Then open:
👉 http://127.0.0.1:8000/docs

### Key Endpoints

| Route | Description |
|-------|-------------|
| `GET /redact` | Redact a specific chunk from preprocessed doc |
| `POST /feedback` | Submit approval/override for a redacted chunk |

Example:

```bash
curl "http://127.0.0.1:8000/redact?doc_id=resume&chunk_index=0"
```

---

## ✏️ Custom Entity Rules (SpaCy EntityRuler)

Define custom patterns in:

```
app/data/custom_patterns.jsonl
```

Sample rule:

```json
{"label": "EMAIL", "pattern": [{"TEXT": {"REGEX": ".*@.*\\..*"}}]}
```

These patterns are loaded at runtime and override/extend the default model.

---

## 🧪 Running Tests

```bash
poetry run pytest -v
```

Includes tests for:
- Redaction logic
- Feedback logging
- Endpoint responses
- FAISS + metadata I/O

---

## 🔮 Next Steps (optional enhancements)

- [ ] Add batch `/redact/all` endpoint
- [ ] Enable `/summarize` using HF Transformers
- [ ] Integrate a frontend review UI
- [ ] Support PDF export of redacted content
