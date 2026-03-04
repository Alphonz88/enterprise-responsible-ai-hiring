
SKILL_WEIGHTS = {
    "python": 30,
    "machine learning": 25,
    "data analysis": 20,
    "sql": 15,
    "communication": 10,
}

SYNONYMS = {
    "python": ["python", "python3"],
    "machine learning": ["ml", "deep learning", "machine learning"],
    "data analysis": ["analytics", "data analytics", "data analysis"],
    "sql": ["sql", "mysql", "postgresql"],
    "communication": ["communication", "presentation", "teamwork"],
}

DECISION_THRESHOLDS = {
    "selected": 70,
    "review": 50,
}

STATUS_MESSAGES = {
    "Selected": "Candidate is Selected based on required weighted skill match.",
    "Review": "Candidate requires further HR review.",
    "Rejected": "Candidate is Rejected due to insufficient core skill match.",
}


def calculate_score(text: str) -> tuple[float, list[str]]:
    """Calculate weighted AI score and return matched skills."""
    text_lower = text.lower()
    matched_skills = []
    total_weight = 0

    for skill, synonyms in SYNONYMS.items():
        for synonym in synonyms:
            if synonym in text_lower:
                if skill not in matched_skills:
                    matched_skills.append(skill)
                    total_weight += SKILL_WEIGHTS[skill]
                break  # No double counting

    score = (total_weight / 100) * 100
    return round(score, 2), matched_skills


def get_decision(score: float) -> str:
    """Return 3-level decision based on score."""
    if score >= DECISION_THRESHOLDS["selected"]:
        return "Selected"
    elif score >= DECISION_THRESHOLDS["review"]:
        return "Review"
    else:
        return "Rejected"


def get_status_message(decision: str) -> str:
    """Return human-readable status message."""
    return STATUS_MESSAGES.get(decision, "Unknown status.")
