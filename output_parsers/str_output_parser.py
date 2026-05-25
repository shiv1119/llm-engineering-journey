from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from model import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AI teacher."),
    ("human", "Explain transformers in simple terms.")
])

parser = StrOutputParser()
chain = prompt | llm | parser

response = chain.invoke({})
print(response)