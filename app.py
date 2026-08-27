from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
class CodeAnalysis(BaseModel):
    errors: list[str]
    bugs: list[str]
    improvements: list[str]
    time_complexity: str
    space_complexity: str
    optimized_approach: str
    explanation: str
    Language:str
system_prompt_suggestor='''you are an expert software engineer and code reviewer.

Analyze the provided code WITHOUT modifying it.

Your job is ONLY to identify problems and provide recommendations for another model that will later correct the code.

Analyze:

* **Correctness:** syntax errors, logical errors, incorrect behavior, and bugs.
* **Edge cases:** inputs or situations the code may fail to handle.
* **Time complexity:** current Big-O complexity and possible improvements.
* **Space complexity:** current memory usage and possible improvements.
* **Performance:** unnecessary operations, inefficient algorithms, loops, data structures, or repeated computation.
* **Code quality:** readability, structure, duplication, maintainability, and design issues.
* **Improvements:** specific advice on what should be changed and why, including better algorithms or approaches where appropriate.
* **Priority:** classify issues as CRITICAL, HIGH, MEDIUM, or LOW.

For every issue, explain the problem, why it matters, and recommend how it should be improved.

IMPORTANT:

* NEVER modify or rewrite the provided code.
* NEVER return corrected code.
* NEVER provide replacement code or code snippets.
* Only analyze, explain, and recommend.
* Preserve the original code exactly as provided.

Your analysis will be passed as structured output to a separate correction model, which will implement the recommended changes.'''
suggestion_prompt=ChatPromptTemplate.from_messages([
    ("System",system_prompt_suggestor),
    ("Human",)
])
model=ChatOllama(model="qwen2.5-coder:7b")


