from langchain_groq import ChatGroq
from prompts.match_prompt import match_prompt

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def match_candidate(resume_data, job_description):
    prompt = match_prompt.format(
        resume_data=resume_data,
        job_description=job_description
    )
    return llm.invoke(prompt)