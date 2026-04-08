def grade(task, action):
    action = action.lower()

    if task == "easy":
        return 1.0 if "hello" in action else 0.0

    if task == "medium":
        return 1.0 if "vnenepo" in action else 0.0

    if task == "hard":
        return 1.0 if action.strip() == "1 2 5 9" else 0.0

    return 0.0
