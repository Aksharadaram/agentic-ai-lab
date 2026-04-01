def decide_intent(user_input):
    if "hello" in user_input:
        return "greet"
    elif "date" in user_input:
        return "date"
    elif "calculate" in user_input:
        return "calculate"
    else:
        return "unknown"