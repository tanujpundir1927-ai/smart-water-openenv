from fastapi import FastAPI
from env import SmartWaterEnv

app = FastAPI()

env = SmartWaterEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(data: dict):
    state, reward, done, _ = env.step(data["action"])
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def state():
    return env.state()
