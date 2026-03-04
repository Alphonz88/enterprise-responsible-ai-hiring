import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from backend import load_csv, process_resumes, get_kpi_summary


def render_sidebar():
    """Render sidebar with selection logic explanation."""
    st.sidebar.title("Selection Logic")
    st.sidebar.markdown("""
    ### Scoring Model
    | Skill | Weight |
    |---|---|
    | Python | 30% |
    | Machine Learning | 25% |
    | Data Analysis | 20% |
    | SQL | 15% |
    | Communication | 10% |

    ### Decision Thresholds
    - **Selected**: Score ≥ 70%
    - **Review**: Score 50–69%
    - **Rejected**: Score < 50%

    ### Synonym Detection
    - Python → python, python3
    - ML → ml, deep learning
    - Data Analysis → analytics, data analytics
    - SQL → sql, mysql, postgresql
    - Communication → presentation, teamwork
    """)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Responsible AI")
    st.sidebar.info(
        "No demographic data used. "
        "Scoring is based solely on skill keywords. "
        "Fully auditable and transparent."
    )


def render_kpis(kpis: dict):
    """Render KPI metric cards."""
    cols = st.columns(4)
    labels = ["Total Applicants", "Selected", "Review", "Rejected"]
    colors = ["#58a6ff", "#3fb950", "#d29922", "#f85149"]
    for i, label in enumerate(labels):
        with cols[i]:
            st.metric(label=label, value=kpis[label])


def render_screening_tab():
    """Render the Candidate Screening tab."""
    st.header("Candidate Screening")
    uploaded_file = st.file_uploader(
        "Upload Resume CSV", type=["csv"],
        help="Upload a CSV file with candidate resumes. Any format accepted."
    )

    if uploaded_file:
        with st.spinner("Processing resumes..."):
            df = load_csv(uploaded_file)
            results = process_resumes(df)
            kpis = get_kpi_summary(results)

        st.success(f"Processed {kpis['Total Applicants']} candidates.")
        render_kpis(kpis)

        st.subheader("Screening Results")

        # Color-code decision column
        def highlight_decision(val):
            color_map = {"Selected": "#3fb950", "Review": "#d29922", "Rejected": "#f85149"}
            color = color_map.get(val, "white")
            return f"color: {color}; font-weight: bold"

        styled = results.style.applymap(highlight_decision, subset=["Decision"])
        st.dataframe(styled, use_container_width=True)

        # Audit CSV download
        csv_bytes = results.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Audit Report (CSV)",
            data=csv_bytes,
            file_name="audit_report.csv",
            mime="text/csv",
        )

        # Responsible AI section
        st.subheader("Responsible AI Governance")
        st.info("""
        - No demographic attributes used (no gender, age, religion, caste, or location)
        - Scoring based solely on transparent weighted skill matching
        - No black-box AI -- every score is fully explainable
        - Audit-ready: full results downloadable as CSV
        """)

        # Store results in session state for Analytics tab
        st.session_state["results"] = results
        st.session_state["kpis"] = kpis


def render_analytics_tab():
    """Render the Analytics Dashboard tab."""
    st.header("Analytics Dashboard")

    if "results" not in st.session_state:
        st.info("Upload a CSV on the Candidate Screening tab to see analytics.")
        return

    results = st.session_state["results"]
    kpis = st.session_state["kpis"]

    col1, col2 = st.columns(2)

    # Pie chart - Decision distribution
    with col1:
        st.subheader("Decision Distribution")
        labels = ["Selected", "Review", "Rejected"]
        sizes = [kpis["Selected"], kpis["Review"], kpis["Rejected"]]
        colors = ["#3fb950", "#d29922", "#f85149"]
        fig1, ax1 = plt.subplots(facecolor="#0d1117")
        ax1.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140,
                textprops={"color": "white"})
        ax1.axis("equal")
        st.pyplot(fig1)

    # Histogram - Score distribution
    with col2:
        st.subheader("AI Score Distribution")
        fig2, ax2 = plt.subplots(facecolor="#0d1117")
        ax2.set_facecolor("#161b22")
        ax2.hist(results["AI Score (%)"], bins=10, color="#58a6ff", edgecolor="#0d1117")
        ax2.set_xlabel("AI Score (%)", color="white")
        ax2.set_ylabel("Number of Candidates", color="white")
        ax2.tick_params(colors="white")
        ax2.axvline(70, color="#3fb950", linestyle="--", label="Selected threshold (70%)")
        ax2.axvline(50, color="#d29922", linestyle="--", label="Review threshold (50%)")
        ax2.legend(facecolor="#161b22", labelcolor="white")
        st.pyplot(fig2)


def run_app():
    """Main app entry point called from main.py."""
    st.title("Enterprise Responsible AI Hiring Dashboard")
    render_sidebar()

    tab1, tab2 = st.tabs(["Candidate Screening", "Analytics Dashboard"])
    with tab1:
        render_screening_tab()
    with tab2:
        render_analytics_tab()

# Allow running directly with: streamlit run app.py
if __name__ == "__main__":
    import main
    main.configure_page()
    main.apply_theme()
    run_app()

