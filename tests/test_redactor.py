from app.services.redactor import redact_text

def test_person_redaction():
    text = "Barack Obama met Angela Merkel."
    result = redact_text(text)

    assert "[REDACTED]" in result["redacted_text"]
    assert any(e["type"] == "PERSON" for e in result["entities"])
    assert len(result["entities"]) >= 2
