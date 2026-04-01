from input_handler import get_input
from tools import TOOLS
from llm_engine import decide_tool_with_llm
from logger import log_step

def run_agent():
    while True:
        user_input = get_input()

        tool_name, tool_input = decide_tool_with_llm(user_input)

        if tool_name in TOOLS:
            tool = TOOLS[tool_name]

            if tool_name == "date":
                result = tool()
            else:
                result = tool(tool_input)

        else:
            result = "No suitable tool found."

        print(result)
        log_step(user_input, tool_name, result)


if __name__ == "__main__":
    run_agent()