from typing import TypedDict


class State(TypedDict):

    code: str

    errors: list[str]

    suggestions: list[str]

    Timecomplexity: str

    possibletime: str

    itterations: int

    codeperfect: bool