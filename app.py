from fastapi import FastAPI
from env import SmartWaterEnv

app = FastAPI()
env = SmartWaterEnv(task="medium")

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(data: dict):
    state, reward, done, info = env.step(data["action"])
    return {"state": state, "reward": reward, "done": done}

@app.get("/state")
def state():
    return env.state()