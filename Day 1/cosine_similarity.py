from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

v1 = np.array([[1, 2, 3]])
v2 = np.array([[1, 2, 4]])

score = cosine_similarity(v1, v2)
print(score)