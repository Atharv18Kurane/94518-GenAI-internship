import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

while True:
    user_input = input("Ask anything: ")
    if user_input == "exit":
        break

    req_data={
        "model": "llama-3.3-70b-versatile",
        "messages":[
            {"role": "user", "content": user_input }

        ],
    }

    time1=time.perf_counter()
    response=requests.post(url,data=json.dumps(req_data),headers=headers)
    time2=time.perf_counter()
    print("status:",response.status_code)
    res=response.json()

    if "choices" in res:
        print(res["choices"][0]["message"]["content"])
    else:
        print("error")
        print(res)

    print(f"Time required: {time2-time1:.2f} sec")
