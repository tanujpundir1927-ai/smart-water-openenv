from fastapi import FastAPI
from env import SmartWaterEnv
import uvicorn

app = FastAPI()
env = SmartWaterEnv()

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(data: dict):
    state, reward, done, _ = env.step(data["action"])
    return {"state": state, "reward": reward, "done": done}

@app.get("/state")
def state():
    return env.state()


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
