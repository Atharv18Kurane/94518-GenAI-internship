from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

llm=init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key=("non_needed")
)

conversation=[]
agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="you are a helpful assistant.Answer in short."
)

while True:
    user_input=input("Ask anything")
    if user_input == "exit":
        break
    conversation.append({"role":"user","content":user_input})
    result=agent.invoke({"messages":conversation})
    print(result)
    ai_msg=result["messages"][-1]
    print("AI:",ai_msg.content)
    conversation=result["messages"]