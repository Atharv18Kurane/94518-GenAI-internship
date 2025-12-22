from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv

load_dotenv()
llm=init_chat_model(
    model= "llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)
k=0
input("enter k value:",k)
conversation= list()
while True:
    user_input=input("You:")
    if user_input==exit:
        break
    user_msg = {"role":"user", "content":user_input}
    conversation.append(user_msg)
    system_msg = conversation[0]
    recent_msgs = conversation[-k * 2:]   # user + assistant pairs
    context = [system_msg] + recent_msgs
    llm_output = llm.invoke(conversation)
    print("AI:",llm_output.content)
    llm_msg = {"role":"assistant","content":llm_output.content}
    conversation.append(llm_msg)


