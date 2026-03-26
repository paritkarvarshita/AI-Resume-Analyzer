import re

skills_list = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "flask", "django"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if re.search(skill, text):
            found_skills.append(skill)

    return list(set(found_skills))