from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
You are an AI recruiter.

Compare candidate data with job description.

Return:
- Matching Skills
- Missing Skills

RULES:
- Only use given data
- Do NOT assume skills
- Be precise

Resume Data:
{resume_data}

Job Description:
{job_description}
"""
)