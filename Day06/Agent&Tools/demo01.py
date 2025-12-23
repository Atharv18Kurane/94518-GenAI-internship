from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

llm=init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key= ("non needed")
)

agent=create_agent(model=llm, tools=[])

result = agent.invoke({"messages":[{"role":"user","content":"what is langchain"}]})

print(result["messages"][-1].content)
