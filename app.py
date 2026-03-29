from flask import Flask, render_template, request
from utils.pdf_reader import extract_text_from_pdf
from ml.skill_extractor import extract_skills
from ml.model import analyze_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", role="", error="")

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():

    # If opened directly
    if request.method == 'GET':
        return render_template("index.html", role="", error="")

    file = request.files.get('resume')
    role = request.form.get('role', "")

    # ❌ No file uploaded
    if not file or file.filename == "":
        return render_template("index.html", role=role, error="⚠ Please upload a file")

    # ❌ Not a PDF
    if not file.filename.lower().endswith(".pdf"):
        return render_template("index.html", role=role, error="⚠ Only PDF files are allowed")

    try:
        text = extract_text_from_pdf(file)
    except Exception:
        return render_template("index.html", role=role, error="⚠ Invalid or corrupted PDF file")

    # ✅ Continue processing
    user_skills = extract_skills(text)

    required_skills, missing_skills, matched_skills = analyze_resume(user_skills, role)

    score = int((len(matched_skills) / len(required_skills)) * 100) if required_skills else 0

    result = {
        "prediction": role,
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