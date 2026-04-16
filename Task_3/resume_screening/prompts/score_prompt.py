from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_result"],
    template="""
You are an AI evaluator.

Assign a score between 0 and 100.

SCORING RULES:
- Strong skill match → high score
- Missing core skills → reduce score
- Experience matters

IMPORTANT:
Return ONLY a number.
Give very low score if core skills like ML/NLP are missing

Match Result:
{match_result}
"""
)