from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from state import State


def suggestions(state: State) -> State:

    class CodeAnalysis(BaseModel):

        errors: list[str] = Field(
            description="Actual correctness or logic errors that would cause the solution to fail."
        )

        suggestions: list[str] = Field(
            description="""
    ONLY include actionable improvements that should actually be made to the code.
    If there are no meaningful improvements, return an EMPTY LIST [].
    NEVER put statements such as "The code is correct" or "No errors".
    """
        )

        Timecomplexity: str = Field(
            description="The time complexity of the current code, e.g. O(n^2)."
        )

        possibletime: str = Field(
            description="""
    The optimal asymptotic time complexity achievable for THIS SPECIFIC PROBLEM (e.g. O(n log n) or O(n)).
    Return exactly ONE Big-O complexity.
    """
        )

        codeperfect: bool = Field(
            description="MUST be False if there are any errors, any suggestions, or if optimal time complexity is better than current time complexity. MUST be True ONLY if code is optimal and bug-free."
        )

    llm = ChatOllama(model="granite3.3:8b")

    structuredmodel = llm.with_structured_output(CodeAnalysis)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a code analysis AI.

Analyse the given code carefully for:
- Correctness and logic errors
- Actionable code improvements & optimizations
- Current time complexity vs. optimal possible time complexity

CRITICAL RULES FOR `codeperfect`:
- Set `codeperfect` to `false` if:
  1. There are any errors or bugs in the code.
  2. There are any suggestions for improvement or optimization.
  3. The current time complexity can be improved (e.g., current is O(n^2) but optimal is O(n log n) or O(n)).
- Set `codeperfect` to `true` ONLY IF the code has zero errors, zero suggestions, and already achieves the optimal time complexity.

Return the analysis according to the provided structured schema."""
        ),
        (
            "human",
            "Analyse this code properly:\n\n{code}"
        )
    ])

    chain = prompt | structuredmodel

    code = state["code"]

    result = chain.invoke({
        "code": code
    })

    # Guardrail: force codeperfect to False if errors or suggestions were found
    is_perfect = result.codeperfect
    if result.errors or result.suggestions:
        is_perfect = False

    return {
        "code": code,
        "errors": result.errors,
        "suggestions": result.suggestions,
        "Timecomplexity": result.Timecomplexity,
        "possibletime": result.possibletime,
        "codeperfect": is_perfect,
        "itterations": state["itterations"]
    }