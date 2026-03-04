import pandas as pd
import io
from utils import detect_name_column, detect_text_columns, combine_text_columns, clean_text
from scoring import calculate_score, get_decision, get_status_message


def load_csv(uploaded_file) -> pd.DataFrame:
    """Load uploaded CSV file into a DataFrame."""
    content = uploaded_file.read()
    df = pd.read_csv(io.BytesIO(content), encoding="utf-8", on_bad_lines="skip")
    df.columns = df.columns.str.strip()
    return df


def process_resumes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full pipeline:
    1. Detect name and text columns
    2. Combine text
    3. Score each candidate
    4. Assign decision and status message
    """
    name_col = detect_name_column(df)
    text_cols = detect_text_columns(df)

    # Exclude name column from text analysis
    if name_col and name_col in text_cols:
        text_cols.remove(name_col)

    combined_text = combine_text_columns(df, text_cols).apply(clean_text)

    results = []
    for i, text in enumerate(combined_text):
        score, matched_skills = calculate_score(text)
        decision = get_decision(score)
        status_msg = get_status_message(decision)
        candidate_name = df[name_col].iloc[i] if name_col else f"Candidate {i + 1}"

        results.append({
            "Candidate Name": candidate_name,
            "AI Score (%)": score,
            "Matched Skills": ", ".join(matched_skills) if matched_skills else "None",
            "Decision": decision,
            "Status Message": status_msg,
        })

    return pd.DataFrame(results)


def get_kpi_summary(results_df: pd.DataFrame) -> dict:
    """Return KPI counts for dashboard display."""
    return {
        "Total Applicants": len(results_df),
        "Selected": len(results_df[results_df["Decision"] == "Selected"]),
        "Review": len(results_df[results_df["Decision"] == "Review"]),
        "Rejected": len(results_df[results_df["Decision"] == "Rejected"]),
    }
