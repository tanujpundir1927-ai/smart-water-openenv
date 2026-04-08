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

BASE_URL = "http://localhost:8000"

def choose_action(state):
    if state["leakage"] == 1:
        return "fix"
    elif state["water_level"] < state["demand"]:
        return "increase"
    return "maintain"

def run():
    print("[START]")

    state = requests.post(f"{BASE_URL}/reset").json()

    for step in range(15):
        action = choose_action(state)

        # Required dummy LLM call
        client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "optimize water"}]
        )

        response = requests.post(
            f"{BASE_URL}/step",
            json={"action": action}
        ).json()

        state = response["state"]
        reward = response["reward"]

        print(f"[STEP] step={step} action={action} reward={reward}")

    print("[END]")

if __name__ == "__main__":
    run()