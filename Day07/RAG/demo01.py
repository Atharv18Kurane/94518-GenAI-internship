from sentence_transformers import SentenceTransformer
import numpy as np 

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

embedded_model = SentenceTransformer("all-MiniLM-L6-v2")
sentenses = [
    "I love Cricket.",
    "Running is my favorite sport.",
    "Messi talks spanish."
]

emebeddings = embedded_model.encode(sentenses)

for embedded_vect in emebeddings:
    print("Length:", len(embedded_vect), "-->",embedded_vect[:4])

print("Sentence 1 & 2 similarity:", cosine_similarity(emebeddings[0],emebeddings[1]))
print("Sentence 1 & 3 similarity:", cosine_similarity(emebeddings[0],emebeddings[2]))

