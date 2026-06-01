# AI Career Copilot

AI Career Copilot is an AI-powered resume and job description analyzer built using Python and Streamlit. It helps users understand their skill alignment with job descriptions, identify missing skills, and receive learning recommendations.

## Live Demo

https://ai-career-copilot-ko2dcnmf5dyx4qgtkhde7g.streamlit.app/

## Features

* Resume PDF Upload
* Job Description Analysis
* Skill Extraction
* Resume–Job Match Score
* Missing Skill Detection
* Learning Recommendations
* Resume & Job Description Preview
* Clean and Professional UI

## Tech Stack

* Python
* Streamlit
* PDFPlumber
* HTML + CSS Styling
* Git & GitHub

## How It Works

1. Upload a resume PDF
2. Paste a job description
3. The system extracts skills from both
4. Match score is calculated
5. Missing skills are identified
6. Learning recommendations are generated

## Project Structure

```text
AI_Career_Copilot/
│
├── app.py
├── helpers.py
├── requirements.txt
├── README.md
└── venv/
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Shivangi808/AI-Career-Copilot.git
```

Go to project folder:

```bash
cd AI-Career-Copilot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Future Improvements

* NLP-based skill matching
* ATS scoring
* Resume improvement suggestions
* Advanced recommendation engine

## Author

**Shivangi Singh**

GitHub: https://github.com/Shivangi808
LinkedIn: https://www.linkedin.com/in/shivangi-singh-b94333368/
