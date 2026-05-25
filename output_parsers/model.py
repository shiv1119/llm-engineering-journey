from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="gemma3:latest",
    temperature=0
)