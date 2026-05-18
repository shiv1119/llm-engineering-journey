from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def text_similarity(text1, text2):
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    similarity_matrix = cosine_similarity(emb1, emb2)
    return similarity_matrix[0][0]

text_pairs = [
    ("The cat sits on the mat", "A feline rests on the rug"),  # Similar
    ("I love machine learning", "Natural language processing is fascinating"),  # Related
    ("The weather is sunny", "Python programming is fun"),  # Different
    ("Deep learning uses neural networks", "Artificial intelligence requires training data")  # Related
]

for text1, text2 in text_pairs:
    sim = text_similarity(text1, text2)
    print(f"Similarity: {sim:.4f}")