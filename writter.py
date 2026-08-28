from initialstate import State
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
def writternode(state:State)->State:
    
    class writtingstruct(BaseModel):
       code:str=Field(description="return the correct code only nothing else ")    
    code=state["code"]   
    model=ChatOllama(model="qwen2.5-coder:7b")
    prompt=ChatPromptTemplate.from_messages(
        [
            ('system','''you are a code writting expert your task is to analyse the code {code} and return the correct code only no statemnets/comments required at all'''),
            
        ]
    )
    structuredllm=model.with_structured_output(writtingstruct)
    chain=prompt | structuredllm
    result=chain.invoke({'code':code})
    return{
        "code":result.code
    }