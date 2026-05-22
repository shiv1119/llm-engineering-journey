# from openai import OpenAI

# client = OpenAI()
# response = client.embeddings.create(
#     model="Text-embedding-3-small",
#     input="Langraph enables stateful AI Agents"
# )
# embedding = response.data[0].embedding

# print(len(embedding))
# print(embedding[:10])  
# Requires open ai key

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-mpnet-base-v2")

text = "Langraph enables stateful Ai Agents"
embeddings = model.encode(text)
print("Embeddings Dimension: ", len(embeddings))
print("First 10 values: ", embeddings[:10])
