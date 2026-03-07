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

### 1. Clone the Repository

Open your terminal or command prompt and run:

git clone https://github.com/Alphonz88/enterprise-responsible-ai-hiring.git

---

### 2. Navigate to the Project Folder

cd enterprise-responsible-ai-hiring

---

### 3. Install Required Dependencies

Make sure Python is installed, then run:

pip install -r requirements.txt

---

### 4. Launch the Application

Start the Streamlit web application:

streamlit run app.py

---

### 5. Open the Web Interface

After running the command, Streamlit will automatically open in your browser.

---

### 6. Upload Resume Dataset

Upload a CSV file containing resumes.
You can also use the provided sample dataset:

AI_Resume_Screening.csv

---

### 7. View AI Evaluation Results

The system will:

• Automatically detect resume text columns
• Calculate weighted skill scores
• Categorize candidates into Selected / Review / Rejected
• Display results on the HR dashboard

---

### 8. Download Audit Report

Click the **Download Results** button to export the candidate evaluation report as a CSV file.


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
