import re

# Base skills
skills_list = [
    "python", "java", "sql", "mysql",
    "machine learning", "data analysis",
    "html", "css", "javascript",
    "flask", "django",
    "pandas", "numpy", "scikit-learn",
    "opencv", "yolo", "react",
    "bootstrap", "spring", "hibernate"
]

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    # Extract words
    words = re.findall(r'\b\w+\b', text)

    for skill in skills_list:

        # Single word skills (java, python, sql)
        if " " not in skill:
            if skill in words:
                found_skills.add(skill)

        # Multi-word skills (machine learning)
        else:
            if skill in text:
                found_skills.add(skill)

    # 🔥 Smart normalization (VERY IMPORTANT)
    if "java" in text:
        found_skills.add("java")

    if "python" in text:
        found_skills.add("python")

    if "mysql" in text or "sql" in text:
        found_skills.add("sql")

    return list(found_skills)