from langchain_groq import ChatGroq
from prompts.extract_prompt import extract_prompt

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def extract_info(resume):
    prompt = extract_prompt.format(resume=resume)
    return llm.invoke(prompt)