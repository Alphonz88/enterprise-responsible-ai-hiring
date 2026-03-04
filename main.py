
import streamlit as st

# Page configuration - must be called before any other Streamlit command
def configure_page():
    st.set_page_config(
        page_title="Enterprise Responsible AI Hiring Dashboard",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

# Dark corporate theme via custom CSS
def apply_theme():
    st.markdown("""
    <style>
        .stApp { background-color: #0d1117; color: #c9d1d9; }
        .stMetric { background-color: #161b22; border-radius: 8px; padding: 10px; }
        .stDataFrame { background-color: #161b22; }
        .stTabs [data-baseweb="tab"] { color: #58a6ff; }
        .stSidebar { background-color: #161b22; }
        h1, h2, h3 { color: #58a6ff; }
    </style>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    configure_page()
    apply_theme()

    # Import and run the main app UI
    from app import run_app
    run_app()
