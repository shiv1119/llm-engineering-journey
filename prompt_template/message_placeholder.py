from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

memory_prompt = ChatPromptTemplate.from_message([
    (
    "system",
    """
    You are a helpful AI assistant.
    Answer professionally.
    """
    ),
    MessagesPlaceholder(
        variable_name = "chat_history"
    ),
    (
        "human",
        "{question}"
    )
])


# Usage

from langchain_core import HumanMessage, AIMessage

chat_history = [
    HumanMessage(content = "What is Docker?"),
    AIMessage(content = "Docker is containerization platform"),
    HumanMessage(content = "Why it is used?")
]

# then we pass this chat message inside the prompt.
"""
response = chain.invoke(
    {
        "chat_history": chat_history,
        "question": "Explain with an example"
    }
)

print(response.content)
"""
