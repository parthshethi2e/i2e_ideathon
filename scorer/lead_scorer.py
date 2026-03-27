def score_lead(lead):
    score = 0
    reasons = []

    role = lead.get("role", "").lower()
    snippet = lead.get("snippet", "").lower()

    if any(x in role for x in ["cto", "ceo", "chief"]):
        score += 50
        reasons.append("Executive decision-maker")

    elif "vp" in role:
        score += 40
        reasons.append("VP-level")

    elif "director" in role:
        score += 30
        reasons.append("Director-level")

    if "clinical" in snippet or "trial" in snippet:
        score += 25
        reasons.append("Relevant domain signal")

    if "linkedin" in lead.get("source", ""):
        score += 20
        reasons.append("Verified profile")

    return {
        **lead,
        "score": score,
        "reasons": reasons
    }