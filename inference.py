import requests

BASE_URL = "http://127.0.0.1:7860"

def choose_action(state):
    if state["leakage"] == 1:
        return "fix"
    elif state["water_level"] < state["demand"]:
        return "increase"
    return "maintain"

def run():
    task = "smart_water"
    total_reward = 0
    steps = 0

    print(f"[START] task={task}", flush=True)

    try:
        state = requests.post(f"{BASE_URL}/reset").json()["state"]

        for step in range(10):
            action = choose_action(state)

            res = requests.post(
                f"{BASE_URL}/step",
                json={"action": action}
            ).json()

            state = res["state"]
            reward = res["reward"]

            total_reward += reward
            steps += 1

            print(f"[STEP] step={step} reward={reward}", flush=True)

    except Exception as e:
        print(f"[ERROR] {e}", flush=True)

    score = total_reward / max(steps, 1)

    print(f"[END] task={task} score={score} steps={steps}", flush=True)

if __name__ == "__main__":
    run()
