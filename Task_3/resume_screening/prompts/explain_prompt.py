from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["match_result", "score"],
    template="""
Explain the score given to the candidate.

Include:
- Strengths
- Missing skills
- Experience relevance

Keep it short and clear.

Score: {score}

Match Result:
{match_result}
"""
)