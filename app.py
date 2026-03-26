from flask import Flask, render_template, request
from utils.pdf_reader import extract_text_from_pdf
from ml.skill_extractor import extract_skills
from ml.model import analyze_resume

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    role = request.form['role']

    # Step 1: Extract text
    text = extract_text_from_pdf(file)

    # Step 2: Extract skills
    skills = extract_skills(text)

    # Step 3: Analyze
    result = analyze_resume(skills, role)

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)