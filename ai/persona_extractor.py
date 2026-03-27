import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

from config.settings import MODEL

load_dotenv()

logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "i2e-lead-gen"
    }
)

def extract_persona(offering):
    prompt = f"""
    Return JSON only:
    {{
        "titles": [],
        "keywords": []
    }}

    Offering: {offering}
    """

    try:
        res = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content

    except Exception as e:
        logger.error(f"Persona extraction failed: {e}")
        return "{}"