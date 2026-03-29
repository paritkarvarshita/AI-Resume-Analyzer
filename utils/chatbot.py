def chatbot_response(user_message, missing_skills, recommendations, best_role):
    msg = user_message.lower()

    if "learn" in msg or "next" in msg:
        if recommendations:
            return f"🎯 To become a {best_role}, you should learn: {', '.join(missing_skills[:3])}."
        else:
            return "✅ You already have strong skills!"

    elif "skills" in msg:
        if missing_skills:
            return "❌ You are missing: " + ", ".join(missing_skills)
        else:
            return "✅ You have all required skills!"

    elif "role" in msg:
        return f"💼 Best role for you is: {best_role}"

    elif "improve" in msg:
        return f"📈 Improve by learning: {', '.join(missing_skills[:3])}"

    else:
        return "🤖 Ask me about skills, improvements, or what to learn next!"