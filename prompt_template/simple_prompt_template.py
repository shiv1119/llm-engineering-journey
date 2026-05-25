from langchain_core.prompts import PromptTemplate

# Simple prompt Template
explanation_prompt = PromptTemplate.from_template(
    """
    You are a senior AI Engineer.
    Explain the following term clearly.
    Topic:
    {topic}

    Explanation:
    """
)

# Usage

formatted = explanation_prompt.format(
    topic="Transformer Architecture"
)

print(formatted)