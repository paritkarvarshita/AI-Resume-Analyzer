def analyze_resume(user_skills, role):

    role_skills = {
        "Data Scientist": [
            "python", "machine learning", "sql", "statistics",
            "pandas", "numpy", "scikit-learn"
        ],

        "Web Developer": [
            "html", "css", "javascript", "flask",
            "react", "bootstrap"
        ],

        "Java Developer": [
            "java", "sql", "spring", "hibernate"
        ],

        "Software Engineer": [
            "python", "java", "sql",
            "data structures", "algorithms"
        ]
    }

    # Normalize
    user_skills = [skill.lower() for skill in user_skills]
    required_skills = role_skills.get(role, [])

    user_set = set(user_skills)
    required_set = set(required_skills)

    missing_skills = list(required_set - user_set)
    matched_skills = list(required_set & user_set)

    return required_skills, missing_skills, matched_skills