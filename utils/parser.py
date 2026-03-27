def extract_people(results):
    leads = []

    for r in results:
        title = r.get("title", "")
        parts = title.split(" - ")

        if len(parts) >= 2:
            leads.append({
                "name": parts[0].strip(),
                "role": parts[1].strip(),
                "company": "Unknown",
                "source": r.get("link", ""),
                "snippet": r.get("snippet", "")
            })

    return leads