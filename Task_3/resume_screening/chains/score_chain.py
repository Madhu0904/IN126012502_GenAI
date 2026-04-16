from langchain_groq import ChatGroq
from prompts.score_prompt import score_prompt

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def score_candidate(match_result):
    prompt = score_prompt.format(match_result=match_result)
    return llm.invoke(prompt)