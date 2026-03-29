from flask import Flask, render_template, request
from utils.pdf_reader import extract_text_from_pdf
from ml.skill_extractor import extract_skills
from ml.model import analyze_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['resume']
    role = request.form['role']

    if file:
        text = extract_text_from_pdf(file)

        # Extract skills
        user_skills = extract_skills(text)

        # Analyze
        required_skills, missing_skills, matched_skills = analyze_resume(user_skills, role)

        result = {
            "prediction": role,
            "user_skills": user_skills,
            "required_skills": required_skills,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }

        return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)