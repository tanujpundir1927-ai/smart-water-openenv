def normalize(score):
    # Ensure strictly between 0 and 1
    if score <= 0:
        return 0.1
    if score >= 1:
        return 0.9
    return score


def grade_easy(state):
    score = 0.5
    if state["water_level"] >= state["demand"]:
        score += 0.3
    if state["leakage"] == 0:
        score += 0.2
    return normalize(score)


def grade_medium(state):
    score = 0.4
    if state["water_level"] >= state["demand"]:
        score += 0.3
    if state["leakage"] == 0:
        score += 0.3
    return normalize(score)


def grade_hard(state):
    score = 0.3
    if state["water_level"] >= state["demand"]:
        score += 0.4
    if state["leakage"] == 0:
        score += 0.3
    return normalize(score)
