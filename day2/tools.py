from datetime import datetime

def calculator_tool(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"

def date_tool():
    return str(datetime.now().date())

def weather_tool(city="unknown"):
    # mock weather (no API needed)
    return f"Weather in {city}: Sunny, 30°C"

def summarizer_tool(text):
    # simple mock summary
    return " ".join(text.split()[:5]) + "..."

TOOLS = {
    "calculate": calculator_tool,
    "date": date_tool,
    "weather": weather_tool,
    "summarize": summarizer_tool
}