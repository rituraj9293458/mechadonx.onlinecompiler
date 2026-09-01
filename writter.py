from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from state import State


def writternode(state: State) -> State:

    class WritingStruct(BaseModel):
        code: str = Field(
            description="Return complete corrected code only."
        )

    code = state["code"]
    suggestions = state.get("suggestions", [])
    errors = state.get("errors", [])

    model = ChatOllama(model="qwen2.5-coder:7b")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a code fixer. Fix the provided code using errors and suggestions. Return complete corrected python code only without explanations, comments, or markdown formatting."
        ),
        (
            "human",
            "Code:\n{code}\n\nErrors:\n{errors}\n\nSuggestions:\n{suggestions}"
        )
    ])

    structuredllm = model.with_structured_output(WritingStruct)

    chain = prompt | structuredllm

    result = chain.invoke({
        "code": code,
        "suggestions": suggestions,
        "errors": errors
    })

    clean_code = result.code.strip()
    if clean_code.startswith("```"):
        lines = clean_code.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        clean_code = "\n".join(lines).strip()

    return {
        "code": clean_code,
        "itterations": state["itterations"] + 1
    }