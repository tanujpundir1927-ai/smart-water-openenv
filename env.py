import random
from graders import grade_easy, grade_medium, grade_hard


class SmartWaterEnv:
    def __init__(self, task="medium"):
        self.task = task
        self.reset()

    def reset(self):
        self.water_level = random.randint(40, 80)
        self.demand = random.randint(30, 70)
        self.leakage = random.choice([0, 1])
        self.time = 0

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

        # Actions
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

        # Leakage effect
        if self.leakage == 1:
            self.water_level -= 5
            reward -= 0.2

        # Demand satisfaction
        if self.water_level >= self.demand:
            reward += 0.4
        else:
            reward -= 0.4

        # Increase time
        self.time += 1

        # ✅ APPLY TASK-SPECIFIC GRADER
        current_state = self.state()

        if self.task == "easy":
            reward = grade_easy(current_state)

        elif self.task == "medium":
            reward = grade_medium(current_state)

        elif self.task == "hard":
            reward = grade_hard(current_state)

        # ✅ Ensure STRICT range (0,1)
        reward = max(0.1, min(0.9, reward))

        return current_state, reward, False, {}
        
    
