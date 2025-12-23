from langchain_openai import OpenAIEmbeddings
import numpy as np 

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

embedded_model = OpenAIEmbeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy_token",
    check_embedding_ctx_length=False
)
sentenses = [
    "I love Cricket.",
    "Running is my favorite sport.",
    "Messi talks spanish."
]

emebeddings = embedded_model.embed_documents(sentenses)

for embedded_vect in emebeddings:
    print("Length:", len(embedded_vect), "-->",embedded_vect[:4])

print("Sentence 1 & 2 similarity:", cosine_similarity(emebeddings[0],emebeddings[1]))
print("Sentence 1 & 3 similarity:", cosine_similarity(emebeddings[0],emebeddings[2]))


