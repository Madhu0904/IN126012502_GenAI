from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI resume parser.

Extract the following:
- Skills
- Tools
- Experience (in years)

STRICT RULES:
- Do NOT assume anything
- Only extract what is present
- If missing, return "Not Found"
- Output MUST be in JSON format

Resume:
{resume}
"""
)