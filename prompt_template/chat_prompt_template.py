from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_message(
    [
        (
            "system",
            """
            You are a senior backend engineering interviewer.
            Ask technical questions and evaluate answers professionally.
            """
        ),
        (
            "human",
            "{questions}"
        )
    ]
)


message = chat_prompt.format_message(
    question = "Explain Docker networking"
)

print(message)