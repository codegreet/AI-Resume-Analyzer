import requests
from config import AI_PROVIDER, GEMINI_API_KEY, GROQ_API_KEY

def analyze_resume_with_ai(resume_text, job_description):
    if AI_PROVIDER == "gemini":
        url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateText"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{
                    "text": f"""You are an AI Resume Evaluator.
Resume:
{resume_text}

Job Description:
{job_description}

Please return a JSON object with:
- skill_coverage_percent (number)
- missing_keywords (list)
- summary (string, e.g., 'Strong in backend and moderate in AI/ML')"""
                }]
            }]
        }
        response = requests.post(f"{url}?key={GEMINI_API_KEY}", json=data, headers=headers)
        result = response.json()
        return result.get("candidates", [{}])[0].get("output_text", "No response")

    elif AI_PROVIDER == "groq":
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You are an AI Resume Evaluator."},
                {"role": "user", "content": f"""Resume:
{resume_text}

Job Description:
{job_description}

Return JSON:
{{
  "skill_coverage_percent": number,
  "missing_keywords": [list],
  "summary": string
}}"""}
            ]
        }
        response = requests.post(url, json=data, headers=headers)
        result = response.json()
        return result["choices"][0]["message"]["content"]
