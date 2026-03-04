import csv
import io

def parse_csv(text: str):
    reader = csv.reader(io.StringIO(text))
    rows = [row for row in reader if any(cell.strip() for cell in row)]
    return rows

def detect_columns(headers: list[str]) -> dict:
    lc = [h.lower() for h in headers]

    def find(patterns):
        for p in patterns:
            for i, h in enumerate(lc):
                if p in h:
                    return i
        return -1

    return {
        "name":       find(["name", "full name", "candidate"]),
        "email":      find(["email", "mail", "e-mail"]),
        "skills":     find(["skill", "skills", "tech", "technologies"]),
        "experience": find(["experience", "exp", "years", "yrs"]),
        "education":  find(["education", "degree", "qualification", "edu"]),
    }

def export_to_csv(results: list[dict]) -> str:
    headers = ["#", "Name", "Email", "Score", "Status", "Matched Skills", "Experience", "Education"]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    for r in results:
        writer.writerow([
            r["row_index"],
            r["name"],
            r["email"],
            r["score"],
            r["status"],
            ", ".join(r["matched_skills"]),
            r["experience"],
            r["education"],
        ])
    return output.getvalue()
