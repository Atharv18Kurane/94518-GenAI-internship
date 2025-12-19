import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DUMMY_KEY")
url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

while True:
    user_input = input("Ask anything: ")
    if user_input == "exit":
        break

    req_data={
        "model": "meta-llama-3.1-8b-instruct",
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

