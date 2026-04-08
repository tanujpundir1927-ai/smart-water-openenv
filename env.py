import random

class SmartWaterEnv:
    def __init__(self, task="medium"):
        self.max_water = 100
        self.task = task
        self.reset()

    def reset(self):
        self.time = 0
        self.water_level = random.randint(50, 80)
        self.demand = random.randint(30, 60)

        if self.task == "easy":
            self.leakage = 0
        elif self.task == "medium":
            self.leakage = random.choice([0, 1])
        else:
            self.leakage = 1

        return self.state()

    def state(self):
        return {
            "water_level": self.water_level,
            "demand": self.demand,
            "leakage": self.leakage,
            "time": self.time
        }

    def step(self, action):
        reward = 0.0

        if action == "reduce":
            self.water_level -= 10
            reward += 0.05
        elif action == "increase":
            self.water_level += 10
            reward += 0.05
        elif action == "maintain":
            reward += 0.1
        elif action == "fix":
            if self.leakage == 1:
                self.leakage = 0
                reward += 0.3
            else:
                reward -= 0.1

        if self.leakage == 1:
            self.water_level -= 5
            reward -= 0.2

        if self.water_level >= self.demand:
            reward += 0.4
        else:
            reward -= 0.4

        if self.water_level > self.max_water:
            reward -= 0.2
        if self.water_level < 0:
            reward -= 0.5

        self.time += 1

        if self.task == "hard":
            self.demand = random.randint(40, 80)
        else:
            self.demand = random.randint(30, 60)

        reward = max(0.0, min(1.0, reward))

        return self.state(), reward, False, {}
    