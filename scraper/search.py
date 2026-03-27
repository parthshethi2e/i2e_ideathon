import requests
import os
import logging
from config.settings import SEARCH_LOCATION

logger = logging.getLogger(__name__)

SERP_API_KEY = os.getenv("SERP_API_KEY")

def search_serpapi(query):
    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY,
        "hl": "en",
        "gl": "us",
        "location": SEARCH_LOCATION
    }

    try:
        res = requests.get(url, params=params)
        data = res.json()

        results = []

        for r in data.get("organic_results", []):
            results.append({
                "title": r.get("title", ""),
                "link": r.get("link", ""),
                "snippet": r.get("snippet", "")
            })

        return results

    except Exception as e:
        logger.error(f"Search failed: {e}")
        return []