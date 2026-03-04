def status_badge_color(status: str) -> str:
    return {
        "Selected": "green",
        "Review":   "orange",
        "Rejected": "red",
    }.get(status, "gray")

def score_bar_color(score: int) -> str:
    if score >= 70:
        return "green"
    if score >= 40:
        return "orange"
    return "red"

def get_histogram_data(results: list[dict]) -> dict:
    bins   = ["0-20", "21-40", "41-60", "61-80", "81-100"]
    counts = [0, 0, 0, 0, 0]
    for r in results:
        s = r["score"]
        if   s <= 20: counts[0] += 1
        elif s <= 40: counts[1] += 1
        elif s <= 60: counts[2] += 1
        elif s <= 80: counts[3] += 1
        else:         counts[4] += 1
    return dict(zip(bins, counts))

def get_top_skills(results: list[dict], top_n: int = 10) -> list[tuple]:
    freq = {}
    for r in results:
        if r["status"] == "Selected":
            for s in r["matched_skills"]:
                freq[s] = freq.get(s, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

def get_avg_score_by_status(results: list[dict]) -> dict:
    groups = {"Selected": [], "Review": [], "Rejected": []}
    for r in results:
        groups[r["status"]].append(r["score"])
    return {
        k: round(sum(v) / len(v)) if v else 0
        for k, v in groups.items()
    }
