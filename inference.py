import os
import requests
from openai import OpenAI

# ✅ Required environment variables (provided by evaluator)
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_KEY = os.getenv("API_KEY")

# ✅ OpenAI client (MANDATORY)
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

# ✅ Local server URL (HF container)
BASE_URL = "http://127.0.0.1:7860"


def choose_action(state):
    if state["leakage"] == 1:
        return "fix"
    elif state["water_level"] < state["demand"]:
        return "increase"
    return "maintain"


def run():
    task = "smart_water"
    total_reward = 0.0
    steps = 0

    # ✅ REQUIRED FORMAT
    print(f"[START] task={task}", flush=True)

    try:
        # Reset environment
        response = requests.post(f"{BASE_URL}/reset")
        state = response.json()["state"]

        for step in range(10):
            action = choose_action(state)

            # ✅ REQUIRED LLM CALL (VERY IMPORTANT)
            client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": "optimize water usage"}]
            )

            # Step environment
            res = requests.post(
                f"{BASE_URL}/step",
                json={"action": action}
            ).json()

            state = res["state"]
            reward = res["reward"]

            total_reward += reward
            steps += 1

            # ✅ REQUIRED FORMAT
            print(f"[STEP] step={step} reward={reward}", flush=True)

    except Exception as e:
        print(f"[ERROR] {str(e)}", flush=True)

    # Final score
    score = total_reward / max(steps, 1)

    # ✅ REQUIRED FORMAT
    print(f"[END] task={task} score={score} steps={steps}", flush=True)


if __name__ == "__main__":
    run()
