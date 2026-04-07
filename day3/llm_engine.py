
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv(override=True)
print("DEBUG GROQ KEY:", os.getenv("GROQ_API_KEY"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def decide_tool_with_llm(user_input):
    prompt = f"""
Choose one tool:
- calculate
- date
- weather
- summarize

Return ONLY:
tool: <tool_name>
input: <input>

User: {user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    return parse_output(output)


def parse_output(output):
    try:
        lines = output.strip().split("\n")
        tool = lines[0].replace("tool:", "").strip().lower()
        tool_input = lines[1].replace("input:", "").strip()
        return tool, tool_input
    except:
        return "unknown", ""