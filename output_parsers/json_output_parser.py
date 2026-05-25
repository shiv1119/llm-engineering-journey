from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from model import llm

parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages([
    (
        "system", 
        """
        Return ONLY valid JSON.
        Format: {{
            "name": "string",
            "skills": ["skill1", "skill2"],
            "experience": integer
        }}
        """
    ),
    ("human", "Generate a backend engineer profile.")
])

chain = prompt | llm | parser

response = chain.invoke({})
print(response)
print(type(response))