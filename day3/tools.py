from datetime import datetime

def calculator_tool(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid calculation"

def date_tool():
    return str(datetime.now().date())

def weather_tool(city="unknown"):
    return f"Weather in {city}: Sunny, 30°C"

def summarizer_tool(text):
    words = text.split()
    return " ".join(words[:5]) + "..." if words else "Nothing to summarize"

TOOLS = {
    "calculate": calculator_tool,
    "date": date_tool,
    "weather": weather_tool,
    "summarize": summarizer_tool
}