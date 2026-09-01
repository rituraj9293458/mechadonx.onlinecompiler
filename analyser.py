import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from state import State

load_dotenv()


def suggestions(state: State) -> State:

    class CodeAnalysis(BaseModel):
        errors: list[str] = Field(
            description="Logic or syntax errors. Empty list [] if none."
        )
        suggestions: list[str] = Field(
            description="Actionable improvements. Empty list [] if none."
        )
        Timecomplexity: str = Field(
            description="Current time complexity e.g. O(n^2)."
        )
        possibletime: str = Field(
            description="Optimal achievable time complexity e.g. O(n log n)."
        )
        codeperfect: bool = Field(
            description="True if code is correct and meets rules, False otherwise."
        )

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=api_key,
        temperature=0
    )

    structuredmodel = llm.with_structured_output(CodeAnalysis)

    iterations = state.get("itterations", 0)

    # Reduced prompt with staged optimization condition
    if iterations < 3:
        instruction = "Focus ONLY on correctness and logic errors. Ignore performance/time complexity optimization for now."
    else:
        instruction = "Check for correctness, logic errors AND optimize time complexity if current is worse than optimal."

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            f"You are a concise code analyzer. {instruction} Return clean structured analysis."
        ),
        (
            "human",
            "Code:\n{code}"
        )
    ])

    chain = prompt | structuredmodel

    code = state["code"]
    result = chain.invoke({"code": code})

    # Staged Guardrails:
    # On iterations < 3: codeperfect is False ONLY if there are logic errors
    # On iterations >= 3: codeperfect is False if there are logic errors OR optimization suggestions
    is_perfect = result.codeperfect
    if result.errors:
        is_perfect = False
    elif iterations >= 3 and result.suggestions:
        is_perfect = False

    return {
        "code": code,
        "errors": result.errors,
        "suggestions": result.suggestions,
        "Timecomplexity": result.Timecomplexity,
        "possibletime": result.possibletime,
        "codeperfect": is_perfect,
        "itterations": iterations
    }