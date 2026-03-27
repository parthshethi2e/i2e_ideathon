import json

def safe_json_parse(text):
    if not text:
        return {}

    clean = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(clean)
    except:
        return {}