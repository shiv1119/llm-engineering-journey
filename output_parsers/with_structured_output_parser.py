from pydantic import BaseModel
from model import llm
from langchain_core.prompts import ChatPromptTemplate

class Resume(BaseModel):
    name: str
    skills: list[str]
    year_of_experience: int

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a expert HR assistant.
        Generate realistic professional resumes.
        """
    ),
    (
        "human",
        "Generate a resume for {role} engineer."
    )
])

structured_llm = llm.with_structured_output(Resume)

chain = prompt | structured_llm
response = chain.invoke({
    "role": "senior backend"
})

print(response)
print(type(response))

