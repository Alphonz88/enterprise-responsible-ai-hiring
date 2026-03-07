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

## How to Run the Project

### Step 1: Download the Project

1. Open the GitHub repository:
   https://github.com/Alphonz88/enterprise-responsible-ai-hiring

2. Click the **Code** button.

3. Select **Download ZIP**.

4. Extract the downloaded ZIP file to your computer.

---

### Step 2: Open the Project Folder

Open the extracted folder in **Command Prompt / Terminal**.

Example:

cd enterprise-responsible-ai-hiring

---

### Step 3: Install Required Libraries

Make sure **Python is installed** on your system.
Then install the required dependencies using:

pip install -r requirements.txt

---

### Step 4: Run the Application

Start the Streamlit web application:

streamlit run app.py

---

### Step 5: Open the Web Application

After running the command, Streamlit will open automatically in your browser.


---

### Step 6: Upload Resume Dataset

Upload a CSV file containing resumes.

You can also use the provided sample dataset:

AI_Resume_Screening.csv

---

### Step 7: View AI Screening Results

The system will:

• Automatically detect the resume text column
• Calculate weighted skill scores
• Categorize candidates into **Selected / Review / Rejected**
• Display results in the HR dashboard

---

### Step 8: Download the Audit Report

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
