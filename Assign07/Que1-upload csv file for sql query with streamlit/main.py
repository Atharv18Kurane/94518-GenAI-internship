import os
import time
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import pandas as pd 
import pandasql as ps
import streamlit as st  

load_dotenv()

st.title("Query Maker")

llm=init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

if "file" not in st.session_state:
    st.session_state.file=None

if "df" not in st.session_state:
    st.session_state.df=None

if "schema" not in st.session_state:
    st.session_state.schema=None

if "messages" not in st.session_state:
    st.session_state.messages= [

    {"role": "system", "content": "You are SQLite expert developer with 10 years of experience."}
]

preview=st.container()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif(msg["role"] == "assistant"):
        if msg["content"]=="Error":
            st.error("Unable to generate SQL for this input ")
        else:
            st.code(msg["content"],language="sql")

