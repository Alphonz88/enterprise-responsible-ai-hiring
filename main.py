import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Resume Screener Pro",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("""
        <style>
            body, .stApp { background-color: #0f1117; color: #e2e8f0; }
            .stTabs [data-baseweb="tab"]         { color: #94a3b8; }
            .stTabs [aria-selected="true"]       { color: #818cf8; border-bottom: 2px solid #818cf8; }
            .stButton > button                   { background: #4f46e5; color: white; border-radius: 8px; }
            .stButton > button:hover             { background: #6366f1; }
            div[data-testid="stMetricValue"]     { color: #818cf8; font-size: 2rem; }
            .stSlider > div > div > div > div    { background: #818cf8; }
        </style>
    """, unsafe_allow_html=True)

def init_state():
    defaults = {
        "csv_rows":           [],
        "csv_headers":        [],
        "column_map":         {},
        "results":            [],
        "skills":             None,
        "selected_threshold": 70,
        "review_threshold":   40,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
