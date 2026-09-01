from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from state import State


def writternode(state: State) -> State:

    class WritingStruct(BaseModel):

        code: str = Field(
            description="Return the complete corrected code only."
        )

    code = state["code"]
    suggestions = state["suggestions"]
    errors = state["errors"]

    model = ChatOllama(model="qwen2.5-coder:7b")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a code writing expert.

            Your task is to fix the given code using the provided
            suggestions and errors.

            Return the complete corrected code only.
            Do not return explanations.
            Do not return markdown.
            Do not return comments."""
        ),
        (
            "human",
            """Code:

{code}

Suggestions:

{suggestions}

Errors:

{errors}
"""
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