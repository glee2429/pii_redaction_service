
# 🕵️‍♀️ PII Redaction and Classification API

This is a minimal FastAPI project that provides an endpoint to detect and redact personally identifiable information (PII) from input text using SpaCy.

---

## 🚀 Features

- `/redact` API endpoint that takes in raw text and returns redacted output + metadata
- Modular redactor service using SpaCy
- Unit test scaffold with pytest
- Supports both pip and Poetry workflows

---

## 🛠️ Project Structure

```
pii_redaction_service/
├── app/
│   ├── api/                  # API route handlers
│   ├── core/                 # Config and constants
│   ├── services/             # PII redaction logic
├── main.py                   # FastAPI entrypoint
├── tests/                    # Unit tests
├── requirements.txt          # Pip-based dependency list
├── pyproject.toml            # Poetry-based project metadata
```

---

## 🐍 Environment Setup

### Option 1: Using `pip` + `requirements.txt`

```bash
python -m venv .venv
source .venv/bin/activate            
pip install --upgrade pip
pip install -r requirements.txt
```

### Option 2: Using Poetry (recommended for local development)

```bash
# Ensure pyproject.toml exists
poetry install --no-root
source $(poetry env info --path)/bin/activate
```

---

## 📦 Running the API Server

```bash
uvicorn main:app --reload
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🔮 TODOs

- Implement SpaCy-based redactor in `services/redactor.py`
- Wire up FastAPI endpoint in `api/endpoints.py`
- Add real test cases in `tests/test_redactor.py`
