import spacy

# Load the model once at module level
nlp = spacy.load("en_core_web_sm")

# Define which entity types you want to redact (you can start with just PERSON)
PII_ENTITY_TYPES = {"PERSON"}

def redact_text(text: str):
    doc = nlp(text)
    redacted_text = text
    redacted_entities = []

    for ent in doc.ents:
        if ent.label_ in PII_ENTITY_TYPES:
            redacted_entities.append({
                "entity": ent.text,
                "type": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            })
            redacted_text = redacted_text.replace(ent.text, "[REDACTED]")
    print(f"Redacted text {redact_text}")
    return {
        "redacted_text": redacted_text,
        "entities": redacted_entities
    }