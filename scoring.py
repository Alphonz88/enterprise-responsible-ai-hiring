import re

DEFAULT_SKILLS = [
    {"name": "React",              "weight": 8, "min_experience": 0},
    {"name": "Python",             "weight": 9, "min_experience": 0},
    {"name": "SQL",                "weight": 7, "min_experience": 0},
    {"name": "JavaScript",         "weight": 8, "min_experience": 0},
    {"name": "Communication",      "weight": 6, "min_experience": 0},
    {"name": "Leadership",         "weight": 5, "min_experience": 0},
    {"name": "Project Management", "weight": 6, "min_experience": 0},
]

def parse_experience_years(text: str) -> float:
    if not text:
        return 0
    lower = text.lower()
    match = re.search(r"(\d+(?:\.\d+)?)\s*(?:\+|-)?\s*(?:years?|yrs?|yr)", lower)
    if match:
        return float(match.group(1))
    bare = re.match(r"^\s*(\d+(?:\.\d+)?)\s*$", lower)
    if bare:
        return float(bare.group(1))
    return 0

def screen_candidates(rows, headers, skills, selected_threshold, review_threshold, column_map):
    def col(key):
        return column_map.get(key, -1)

    total_weight = sum(s["weight"] for s in skills)
    results = []

    for idx, row in enumerate(rows):
        def get(c):
            return row[c] if c >= 0 and c < len(row) else ""

        name       = get(col("name"))
        email      = get(col("email"))
        skills_txt = get(col("skills"))
        experience = get(col("experience"))
        education  = get(col("education"))

        all_text       = " ".join(row).lower()
        exp_years      = parse_experience_years(experience)
        matched_skills = []
        weighted_score = 0

        for skill in skills:
            if skill["name"].lower() in all_text:
                min_exp = skill.get("min_experience", 0)
                if min_exp > 0 and exp_years < min_exp:
                    matched_skills.append(f"{skill['name']} (exp. req. not met)")
                    weighted_score += skill["weight"] * 0.5
                else:
                    matched_skills.append(skill["name"])
                    weighted_score += skill["weight"]

        score = round((weighted_score / total_weight) * 100) if total_weight > 0 else 0

        if score >= selected_threshold:
            status = "Selected"
        elif score >= review_threshold:
            status = "Review"
        else:
            status = "Rejected"

        results.append({
            "row_index":      idx + 1,
            "name":           name,
            "email":          email,
            "skills":         skills_txt,
            "experience":     experience,
            "education":      education,
            "score":          score,
            "status":         status,
            "matched_skills": matched_skills,
        })

    return results
