from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
import dotenv
dotenv.load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=api_key)

# llm_url="http://127.0.0.1:1234/v1"
# llm=ChatOpenAI(
#     base_url=llm_url,
#     model="meta-llama-3.1-8b-instruct",
#     api_key="dummy_api_key"
# )

user_input=input("Ask anything")
# result = llm.invoke(user_input)
# print("AI: ", result.content)
result = llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")