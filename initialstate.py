from langgraph.graph import StateGraph, START, END

from state import State
from analyser import suggestions
from writter import writternode


with open("code.py", "r", encoding="utf-8") as file:
    user_code = file.read()


initial_state: State = {
    "code": user_code,

    "errors": [],

    "suggestions": [],

    "Timecomplexity": "",

    "possibletime": "",

    "itterations": 0,

    "codeperfect": False
}


def checker(state: State) -> bool:

    if state["itterations"] >= 6:
        return True

    if state["codeperfect"] is True and not state["errors"] and not state["suggestions"]:
        return True

    return False


graph = StateGraph(State)

graph.add_node("analyser", suggestions)

graph.add_node("writter", writternode)

graph.add_edge(START, "analyser")

graph.add_conditional_edges(
    "analyser",
    checker,
    {
        True: END,
        False: "writter"
    }
)

graph.add_edge("writter", "analyser")


workflow = graph.compile()