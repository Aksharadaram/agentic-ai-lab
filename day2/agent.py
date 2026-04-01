from input_handler import get_input
from decision_engine import decide_tool
from tools import TOOLS

def run_agent():
    while True:
        user_input = get_input()
        tool_name = decide_tool(user_input)

        if tool_name in TOOLS:
            tool = TOOLS[tool_name]

            if tool_name == "calculate":
                expression = user_input.replace("calculate", "")
                result = tool(expression)

            elif tool_name == "weather":
                city = user_input.replace("weather", "").strip()
                result = tool(city)

            elif tool_name == "summarize":
                text = user_input.replace("summarize", "")
                result = tool(text)

            else:
                result = tool()

            print(result)

        else:
            print("No suitable tool found.")


if __name__ == "__main__":
    run_agent()