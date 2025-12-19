import streamlit as st
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
st.title("My Chatbot")

# ================== GROQ CONFIG ==================
api_key = os.getenv("GROQ_API_KEY")
groq_url = "https://api.groq.com/openai/v1/chat/completions"
groq_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("Menu")
    mode = st.selectbox("Select Menu", ["Cloud Based API", "Local API"])

# ================== GROQ ==================
if mode == "Cloud Based API":
    user_input = st.chat_input("Ask anything")

    if user_input:
        req_data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(
            groq_url,
            headers=groq_headers,
            json=req_data
        )

        # 1️⃣ HTTP-level check
        if response.status_code != 200:
            st.error(f"HTTP Error {response.status_code}")
            st.code(response.text)
        else:
            res = response.json()

            # 2️⃣ API-level check
            if "choices" not in res:
                st.error("Groq API Error")
                st.json(res)
            else:
                st.success(res["choices"][0]["message"]["content"])

# ================== LM STUDIO ==================
if mode == "Local API":
    lm_url = "http://127.0.0.1:1234/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    user_input = st.chat_input("Ask anything")

    if user_input:
        req_data = {
            "model": "meta-llama-3.1-8b-instruct",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(
            lm_url,
            headers=headers,
            json=req_data
        )

        # 1️⃣ HTTP-level check
        if response.status_code != 200:
            st.error(f"HTTP Error {response.status_code}")
            st.code(response.text)
        else:
            res = response.json()

            # 2️⃣ API-level check
            if "choices" not in res:
                st.error("LM Studio API Error")
                st.json(res)
            else:
                st.success(res["choices"][0]["message"]["content"])
