import os
import requests
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

BASE_URL = "http://127.0.0.1:7860"

def choose_action(state):
    if state["leakage"] == 1:
        return "fix"
    elif state["water_level"] < state["demand"]:
        return "increase"
    return "maintain"

def run():
    print("[START]")

    try:
        state = requests.post(f"{BASE_URL}/reset").json()

        for step in range(10):
            action = choose_action(state)

            response = requests.post(
                f"{BASE_URL}/step",
                json={"action": action}
            ).json()

            state = response["state"]
            reward = response["reward"]

            print(f"[STEP] step={step} action={action} reward={reward}")

    except Exception as e:
        print("[ERROR]", str(e))

    print("[END]") 
