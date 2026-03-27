from ai.persona_extractor import extract_persona
from scraper.search import search_serpapi
from utils.parser import extract_people
from utils.helpers import safe_json_parse
from scorer.lead_scorer import score_lead
from config.settings import EXEC_TITLES, DEFAULT_DOMAIN, MAX_RESULTS

def build_query(persona, offering):
    titles = persona.get("titles", [])
    keywords = persona.get("keywords", [])

    title_part = " OR ".join([t.lower() for t in titles[:3]] + EXEC_TITLES)
    keyword_part = " OR ".join(keywords[:3]) if keywords else offering

    domain_part = " OR ".join(DEFAULT_DOMAIN)

    return f'''
    site:linkedin.com/in
    ({title_part})
    ({keyword_part})
    ({domain_part})
    ("current" OR "present")
    -jobs -hiring
    '''

def run_pipeline(offering):

    persona_raw = extract_persona(offering)
    persona = safe_json_parse(persona_raw)

    query = build_query(persona, offering)

    results = search_serpapi(query)
    leads = extract_people(results)

    leads = [l for l in leads if isinstance(l, dict)]

    scored = [score_lead(l) for l in leads]
    ranked = sorted(scored, key=lambda x: x["score"], reverse=True)

    return {
        "persona": persona,
        "query": query,
        "leads": ranked[:MAX_RESULTS]
    }