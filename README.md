# AI Resume Analyzer

AI Resume Analyzer is a Machine Learning and NLP-based web application that analyzes resumes and identifies skill gaps based on job roles.

##  Features
- Upload resume (PDF)
- Extract text using NLP
- Identify skills
- Compare with job role requirements
- Show missing skills (skill gap analysis)
- Flask-based web app

##  Technologies Used
- Python
- Flask
- spaCy (NLP)
- scikit-learn
- pdfplumber
- HTML, CSS
- Machine Learning

## Project Structure
AI_Resume_Analyzer/
- app.py
- data/
- ml/
- static/
- templates/
- utils/

##  How to Run ?
1. Install libraries:
   pip install flask pandas spacy pdfplumber scikit-learn

2. Download NLP model:
   python -m spacy download en_core_web_sm

3. Run app:
   python app.py

4. Open:
   http://127.0.0.1:5000/

##  Future Scope
- Improve UI design
- Add job recommendations
- Deploy online
- Advanced ML model

##  Author
Varshita Paritkar
