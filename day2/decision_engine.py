def decide_tool(user_input):
    if "calculate" in user_input:
        return "calculate"
    elif "date" in user_input:
        return "date"
    elif "weather" in user_input:
        return "weather"
    elif "summarize" in user_input:
        return "summarize"
    else:
        return "unknown"