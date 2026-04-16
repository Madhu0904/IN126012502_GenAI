from langchain_groq import ChatGroq
from prompts.explain_prompt import explain_prompt

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def explain_candidate(match_result, score):
    prompt = explain_prompt.format(
        match_result=match_result,
        score=score
    )
    return llm.invoke(prompt)