from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

from initialstate import State
def suggestions(state: State) -> State:

    class CodeAnalysis(BaseModel):

        errors: list[str] = Field(
            description="Actual correctness or logic errors that would cause the solution to fail."
        )

        suggestions: list[str] = Field(
            description="Improvements needed to make the code correct or better. Return an empty list if there are no suggestions."
        )

        Timecomplexity: str = Field(
            description="The time complexity of the current code."
        )

        possibletime: str = Field(
            description="The most suitable possible time complexity for this problem."
        )

        codeperfect: bool = Field(
            description="True only if the code is correct and cannot be meaningfully improved. Otherwise False."
        )

    llm = ChatOllama(model="deepseek-r1:8b")

    Structuredmodel = llm.with_structured_output(CodeAnalysis)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a code analysis AI.
               Analyse the given code carefully for correctness, logic errors,
               possible improvements, and time complexity.
               Return the analysis according to the provided structured fields."""
                                      ),
        (
           
            "human",
            "Analyse this code properly:\n\n{code}"
        )
    ])

    chain = prompt | Structuredmodel

    code = state["code"]

    result = chain.invoke({
        "code": code
    })

    return {
        "code": code,
        "errors": result.errors,
        "suggestions": result.suggestions,
        "Timecomplexity": result.Timecomplexity,
        "possibletime": result.possibletime,
        "codeperfect": result.codeperfect
    }

