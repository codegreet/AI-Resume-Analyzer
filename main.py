import os
from utils.pdf_extractor import extract_text_from_pdf
from utils.ai_analyzer import analyze_resume_with_ai

def main():
    # === Input ===
    resume_path = "resumes/sample_resume.pdf"
    job_description = """
    Looking for a Software Engineer skilled in Python, FastAPI, SQL, Machine Learning, and REST APIs.
    """

    # === Step 1: Extract text ===
    print("📄 Extracting text from resume...")
    resume_text = extract_text_from_pdf(resume_path)

    # === Step 2: Analyze with AI ===
    print("🤖 Analyzing resume using AI...")
    ai_result = analyze_resume_with_ai(resume_text, job_description)

    # === Step 3: Save Output ===
    os.makedirs("output", exist_ok=True)
    output_file = "output/analysis_report.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(ai_result))

    print(f"\n✅ Analysis complete! Check {output_file}")

if __name__ == "__main__":
    main()
