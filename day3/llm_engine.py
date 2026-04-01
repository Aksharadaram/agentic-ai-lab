def decide_tool_with_llm(user_input):
    user_input = user_input.lower().strip()

    # Simulated reasoning layer

    # Calculation detection
    if any(op in user_input for op in ["+", "-", "*", "/"]) or "calculate" in user_input:
        expression = user_input.replace("calculate", "").strip()
        return "calculate", expression

    # Date detection
    elif "date" in user_input or "today" in user_input:
        return "date", ""

    # Weather detection
    elif "weather" in user_input:
        words = user_input.split()
        city = words[-1] if len(words) > 1 else "unknown"
        return "weather", city

    # Summarization detection
    elif "summarize" in user_input or "summary" in user_input:
        text = user_input.replace("summarize", "").replace("summary", "").strip()
        return "summarize", text

    # Unknown intent
    else:
        return "unknown", ""