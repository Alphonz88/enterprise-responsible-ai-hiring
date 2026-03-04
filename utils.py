import pandas as pd
import re


def clean_text(text) -> str:
    """Lowercase and strip extra whitespace from text."""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def detect_name_column(df: pd.DataFrame) -> str | None:
    """Auto-detect the name column by common column name patterns."""
    name_patterns = ["name", "full name", "fullname", "candidate", "applicant", "person"]
    for col in df.columns:
        if any(pattern in col.lower() for pattern in name_patterns):
            return col
    return None


def detect_text_columns(df: pd.DataFrame) -> list[str]:
    """Auto-detect columns likely containing resume text (string columns with long content)."""
    text_cols = []
    for col in df.columns:
        if df[col].dtype == object:
            avg_len = df[col].dropna().astype(str).apply(len).mean()
            if avg_len > 20:  # Threshold: columns with meaningful text length
                text_cols.append(col)
    return text_cols


def combine_text_columns(df: pd.DataFrame, text_cols: list[str]) -> pd.Series:
    """Combine multiple text columns into a single string per row."""
    return df[text_cols].fillna("").astype(str).agg(" ".join, axis=1)
