# Enterprise Responsible AI Hiring System

### AI4Dev '26 Hackathon Submission

**Domain:** Responsible AI & Resource Optimization

---

## Problem Statement

Modern companies receive thousands of resumes for a single job opening.
Manual screening is slow, inconsistent, and prone to bias.

Existing AI-based hiring tools often:

* Lack transparency
* Use black-box scoring
* Do not provide clear rejection reasons
* Risk demographic bias

There is a need for a **transparent, fair, and audit-ready AI hiring system**.

---

## Our Solution

We built a **transparent AI-powered resume screening system** that:

* Accepts bulk CSV resume uploads

* Automatically detects resume text columns

* Uses weighted skill-based scoring

* Categorizes candidates into:

  * **Selected (≥ 70%)**
  * **Review (50–69%)**
  * **Rejected (< 50%)**

* Avoids using any demographic attributes

* Generates downloadable audit reports

---

## Key Features

* CSV Upload (Bulk Resume Processing)
* Automatic Column Detection
* Weighted Skill Scoring
* Intelligent Synonym Detection
* 3-Category Decision System
* Professional HR Dashboard
* Downloadable Audit Report
* Responsible AI Compliance

---

## Responsible AI Principles Followed

This system follows **Responsible AI best practices**:

* No use of gender, age, religion, caste, or location
* Transparent scoring logic
* Explainable matched skill display
* Human-review stage included
* Audit-ready output

---

## System Architecture

```
Resume CSV Upload
        ↓
Data Processing (Pandas)
        ↓
Skill Extraction (Regex + Synonym Matching)
        ↓
Weighted Scoring Engine
        ↓
Decision Model (Selected / Review / Rejected)
        ↓
HR Dashboard + Audit Report
```

---

## Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib
* Regex-based NLP

---

## How to Run Locally

Clone the repository:

```
git clone https://github.com/Alphonz88/enterprise-responsible-ai-hiring
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## Repository Structure

```
app.py
requirements.txt
README.md
```

---

## Demo

Demo Video:
(Add your video link here)

---
