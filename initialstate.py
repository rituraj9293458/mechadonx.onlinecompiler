from typing import TypedDict
class State(TypedDict):
    code:str
    errors:list[str]
    suggestions:list[str]
    Timecomplexity:str
    possibletime:str
   
    codeperfect:bool
with open("code.py", "r", encoding="utf-8") as file:
    user_code = file.read()    
initial_state = {
   "code": user_code,
   "errors": [],
   "suggestions": [],
   "Timecomplexity": "",
   "possibletime": "",
   
   "codeperfect": False 
}    