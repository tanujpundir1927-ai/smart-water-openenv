def grade_easy(state):
    return 1.0 if state["water_level"] >= state["demand"] else 0.6

def grade_medium(state):
    score = 0.0
    if state["leakage"] == 0:
        score += 0.5
    if state["water_level"] >= state["demand"]:
        score += 0.5
    return min(score, 1.0)

def grade_hard(state):
    score = 0.0
    if state["leakage"] == 0:
        score += 0.4
    if state["water_level"] >= state["demand"]:
        score += 0.4
    if state["water_level"] <= 100:
        score += 0.2
    return min(score, 1.0)