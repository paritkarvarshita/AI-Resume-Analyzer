job_roles = {
    "Data Scientist": ["python", "machine learning", "data analysis", "sql"],
    "Web Developer": ["html", "css", "javascript", "flask"],
    "Software Engineer": ["java", "python", "sql"]
}

def analyze_resume(user_skills, role):
    required_skills = job_roles.get(role, [])

    missing_skills = list(set(required_skills) - set(user_skills))

    return {
        "required_skills": required_skills,
        "user_skills": user_skills,
        "missing_skills": missing_skills
    }