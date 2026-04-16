from dotenv import load_dotenv
load_dotenv()

from chains.extract_chain import extract_info
from chains.match_chain import match_candidate
from chains.score_chain import score_candidate
from chains.explain_chain import explain_candidate


# Job Description
job_description = """
We are hiring a Data Scientist.

Requirements:
- Python, Machine Learning, Deep Learning
- NLP, Pandas, NumPy
- TensorFlow or PyTorch
- Data Visualization
- 2+ years experience
"""


# Resumes
resume_strong = """
John Doe
Skills: Python, Machine Learning, Deep Learning, NLP, Pandas, NumPy, TensorFlow, PyTorch
Experience: 3 years as Data Scientist
"""

resume_avg = """
Jane Smith
Skills: Python, Pandas, Data Analysis
Experience: 1 year
"""

resume_weak = """
Sam Lee
Skills: Excel, Communication
Experience: Fresher
"""


def run_pipeline(resume, label):
    print(f"\n===== {label} =====")

    extracted = extract_info(resume)
    matched = match_candidate(extracted.content, job_description)
    score = score_candidate(matched.content)
    explanation = explain_candidate(matched.content, score.content)

    print("\nExtracted:", extracted.content)
    print("\nMatched:", matched.content)
    print("\nScore:", score.content)
    print("\nExplanation:", explanation.content)


if __name__ == "__main__":
    run_pipeline(resume_strong, "STRONG CANDIDATE")
    run_pipeline(resume_avg, "AVERAGE CANDIDATE")
    run_pipeline(resume_weak, "WEAK CANDIDATE")