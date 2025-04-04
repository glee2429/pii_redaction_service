import spacy
from spacy.pipeline import EntityRuler
from pathlib import Path

# Load the model once at module level
nlp = spacy.load("en_core_web_sm")

# Add custom entity rules
ruler = EntityRuler(nlp, overwrite_ents=True)
patterns_path = Path("app/data/custom_patterns.jsonl")
if patterns_path.exists():
    ruler.from_disk(str(patterns_path))
    nlp.add_pipe(ruler, before="ner")


def redact_text(text: str):
    doc = nlp(text)
    redacted_text = text
    redacted_entities = []

    for ent in doc.ents:
        if ent.label_ in {"EMAIL", "PHONE", "TITLE", "PERSON", "GPE"}:  # Redact based on model + rule-based NER
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