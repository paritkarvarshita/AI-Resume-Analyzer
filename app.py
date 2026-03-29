from flask import Flask, render_template, request
from utils.pdf_reader import extract_text_from_pdf
from ml.skill_extractor import extract_skills
from ml.model import analyze_resume
import pickle

app = Flask(__name__)

# 🔥 Load ML model
model = pickle.load(open("ml/model.pkl", "rb"))
vectorizer = pickle.load(open("ml/vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html", error="")

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():

    role_map = {
        "INFORMATION-TECHNOLOGY": [
            "Software Engineer",
            "Full Stack Developer",
            "Backend Developer",
            "Frontend Developer",
            "Web Developer"
        ],
        "DATA SCIENCE": [
            "Data Scientist",
            "Machine Learning Engineer",
            "Data Analyst",
            "AI Engineer"
        ],
        "JAVA DEVELOPER": [
            "Java Developer",
            "Backend Developer"
        ],
        "WEB DESIGNING": [
            "Web Developer",
            "Frontend Developer",
            "UI Developer"
        ],
        "HR": [
            "HR Executive",
            "Recruiter"
        ]
    }

    if request.method == 'GET':
        return render_template("index.html", error="")

    file = request.files.get('resume')

    if not file or file.filename == "":
        return render_template("index.html", error="⚠ Please upload a file")

    if not file.filename.lower().endswith(".pdf"):
        return render_template("index.html", error="⚠ Only PDF files are allowed")

    try:
        text = extract_text_from_pdf(file)
    except Exception:
        return render_template("index.html", error="⚠ Invalid or corrupted PDF file")

    # 🔥 Predict role
    clean_input = [text.lower()]
    vector_input = vectorizer.transform(clean_input)
    predicted_role = model.predict(vector_input)[0]

    # Extract skills
    user_skills = extract_skills(text)

    # 🔥 Map roles
    predicted_role_upper = predicted_role.upper()
    possible_roles = role_map.get(predicted_role_upper, ["Software Engineer"])

    # 🔥 Rank roles
    role_scores = []

    for role in possible_roles:
        required_skills, missing_skills, matched_skills = analyze_resume(user_skills, role)

        if required_skills:
            score = int((len(matched_skills) / len(required_skills)) * 100)
        else:
            score = 0

        role_scores.append({
            "role": role,
            "score": score,
            "matched": matched_skills,
            "missing": missing_skills,
            "required": required_skills
        })

    # Sort roles
    role_scores = sorted(role_scores, key=lambda x: x["score"], reverse=True)

    # 🔥 DEFINE BEST
    best = role_scores[0]

    # Extract best values
    required_skills = best["required"]
    matched_skills = best["matched"]
    missing_skills = best["missing"]
    score = best["score"]
    best_role = best["role"]

    # 🔥 Best role
    best_role = role_scores[0]["role"]
    required_skills = best["required"]
    matched_skills = role_scores[0]["matched"]
    missing_skills = role_scores[0]["missing"]
    score = role_scores[0]["score"]

    result = {
        "prediction": best_role,
        "ranked_roles": role_scores,
        "user_skills": user_skills,
        "required_skills": required_skills, 
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "filename": file.filename,
        "score": score
    }

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)