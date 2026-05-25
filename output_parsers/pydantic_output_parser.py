from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from model import llm

class UserProfile(BaseModel):
    name: str = Field(description = "User full name")
    skills: list[str]
    experience: int

parser = PydanticOutputParser(
    pydantic_object=UserProfile
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Generate user profile.
        {format_instructions}
        """
    ),
    ("human", "Generate a backend engineer profile.")
])

prompt = prompt.partial(
    format_instructions = parser.get_format_instructions()
)

chain = prompt | llm | parser
response = chain.invoke({})
print(response)
print(type(response))
print("-"*10)
print(response.name)
print(response.skills)
print(response.experience)