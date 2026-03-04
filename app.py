import pandas as pd
import streamlit as st

import backend
import main as cfg
import utils
from scoring import DEFAULT_SKILLS, screen_candidates

cfg.setup_page()
cfg.init_state()

if st.session_state["skills"] is None:
    st.session_state["skills"] = [dict(s) for s in DEFAULT_SKILLS]

st.title("Resume Screener Pro")
st.caption("Upload a candidate CSV, configure skill weights, and screen at scale.")

tabs = st.tabs(["Upload", "Configure", "Results", "Dashboard"])

# ── UPLOAD ──────────────────────────────────────────────────────────────────
with tabs[0]:
    st.subheader("Upload Candidates CSV")
    file = st.file_uploader("Drop your CSV here", type=["csv"])
    if file:
        text = file.read().decode("utf-8", errors="replace")
        rows = backend.parse_csv(text)
        if rows:
            headers = rows[0]
            data_rows = rows[1:]
            st.session_state["csv_headers"] = headers
            st.session_state["csv_rows"]    = data_rows
            st.session_state["column_map"]  = backend.detect_columns(headers)
            st.success(f"Loaded {len(data_rows)} candidates with {len(headers)} columns.")
            st.dataframe(pd.DataFrame(data_rows[:5], columns=headers), use_container_width=True)

# ── CONFIGURE ────────────────────────────────────────────────────────────────
with tabs[1]:
    st.subheader("Skill Weights")
    skills = st.session_state["skills"]

    for i, skill in enumerate(skills):
        c1, c2, c3, c4 = st.columns([3, 2, 3, 1])
        with c1:
            skill["name"] = st.text_input(f"Skill {i+1}", value=skill["name"], key=f"name_{i}", label_visibility="collapsed")
        with c2:
            skill["min_experience"] = st.number_input("Min Exp (yrs)", min_value=0, max_value=30,
                                                       value=skill.get("min_experience", 0),
                                                       key=f"exp_{i}", label_visibility="collapsed")
        with c3:
            skill["weight"] = st.slider("Weight", 1, 10, value=skill["weight"], key=f"w_{i}", label_visibility="collapsed")
        with c4:
            if st.button("X", key=f"del_{i}"):
                skills.pop(i)
                st.rerun()

    if st.button("+ Add Skill"):
        skills.append({"name": "", "weight": 5, "min_experience": 0})
        st.rerun()

    st.divider()
    st.subheader("Thresholds")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["selected_threshold"] = st.slider(
            "Selected Threshold", 0, 100, st.session_state["selected_threshold"], 5)
    with col2:
        st.session_state["review_threshold"] = st.slider(
            "Review Threshold", 0, st.session_state["selected_threshold"] - 5,
            min(st.session_state["review_threshold"], st.session_state["selected_threshold"] - 5), 5)

    n = len(st.session_state["csv_rows"])
    st.caption(f"Will screen {n} candidates" if n else "Upload a CSV first.")

    if st.button("Run Screening", type="primary", disabled=(n == 0)):
        valid_skills = [s for s in skills if s["name"].strip()]
        results = screen_candidates(
            st.session_state["csv_rows"],
            st.session_state["csv_headers"],
            valid_skills,
            st.session_state["selected_threshold"],
            st.session_state["review_threshold"],
            st.session_state["column_map"],
        )
        st.session_state["results"] = results
        st.success(f"Screening complete! {len(results)} candidates processed.")

# ── RESULTS ──────────────────────────────────────────────────────────────────
with tabs[2]:
    results = st.session_state["results"]
    if not results:
        st.info("Run screening first.")
    else:
        st.subheader(f"Results -- {len(results)} Candidates")
        search = st.text_input("Search by name or email", "")
        status_filter = st.selectbox("Filter by status", ["All", "Selected", "Review", "Rejected"])

        filtered = results
        if search:
            q = search.lower()
            filtered = [r for r in filtered if q in r["name"].lower() or q in r["email"].lower()]
        if status_filter != "All":
            filtered = [r for r in filtered if r["status"] == status_filter]

        df = pd.DataFrame([{
            "#":             r["row_index"],
            "Name":          r["name"],
            "Email":         r["email"],
            "Score":         r["score"],
            "Status":        r["status"],
            "Matched Skills":r["matched_skills"],
            "Experience":    r["experience"],
            "Education":     r["education"],
        } for r in filtered])

        st.dataframe(df, use_container_width=True)

        csv_export = backend.export_to_csv(filtered)
        st.download_button("Export Audit CSV", csv_export, "audit_report.csv", "text/csv")

# ── DASHBOARD ────────────────────────────────────────────────────────────────
with tabs[3]:
    results = st.session_state["results"]
    if not results:
        st.info("Run screening first to see analytics.")
    else:
        total    = len(results)
        selected = [r for r in results if r["status"] == "Selected"]
        review   = [r for r in results if r["status"] == "Review"]
        rejected = [r for r in results if r["status"] == "Rejected"]
        avg_score = round(sum(r["score"] for r in results) / total)

        st.subheader("Analytics Dashboard")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Candidates", total,    f"Avg score: {avg_score}")
        c2.metric("Selected",          len(selected), f"{round(len(selected)/total*100)}%")
        c3.metric("Review",            len(review),   f"{round(len(review)/total*100)}%")
        c4.metric("Rejected",          len(rejected), f"{round(len(rejected)/total*100)}%")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Status Distribution**")
            status_df = pd.DataFrame({
                "Status": ["Selected", "Review", "Rejected"],
                "Count":  [len(selected), len(review), len(rejected)],
            })
            st.bar_chart(status_df.set_index("Status"))

        with col2:
            st.markdown("**Score Distribution**")
            hist = utils.get_histogram_data(results)
            st.bar_chart(pd.DataFrame(hist.items(), columns=["Range", "Count"]).set_index("Range"))

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Top Skills (Selected Candidates)**")
            top = utils.get_top_skills(results)
            if top:
                skills_df = pd.DataFrame(top, columns=["Skill", "Count"]).set_index("Skill")
                st.bar_chart(skills_df)

        with col4:
            st.markdown("**Avg Score by Status**")
            avgs = utils.get_avg_score_by_status(results)
            st.bar_chart(pd.DataFrame(avgs.items(), columns=["Status", "Avg Score"]).set_index("Status"))
