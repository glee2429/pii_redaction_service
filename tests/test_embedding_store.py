from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_redact_route():
    # Make sure the doc and metadata exist first
    response = client.get("/redact", params={"doc_id": "ediscovery", "chunk_index": 0})
    assert response.status_code == 200
    assert "redacted" in response.json()
