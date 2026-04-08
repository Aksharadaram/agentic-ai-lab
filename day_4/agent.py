# agent.py

import os
import ast
from dotenv import load_dotenv
from groq import Groq

from tools import (
    extract_numbers,
    calculate_sum,
    calculate_average,
    find_max,
    find_min,
    summarize_result
)

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ✅ LLM-based planner (with strict prompt + fallback)
def plan_steps(query):
    prompt = f"""
    You are an AI planner.

    Available steps:
    - extract_numbers
    - sum
    - average
    - max
    - min
    - summarize

    IMPORTANT:
    Return ONLY a Python list.
    Do NOT add explanation.

    Example:
    ["extract_numbers", "average", "summarize"]

    Query: {query}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    print("LLM Raw Output:", text)  # Debug (can remove later)

    try:
        steps = ast.literal_eval(text)
    except:
        # ✅ Fallback logic
        steps = []

        if "average" in text:
            steps = ["extract_numbers", "average", "summarize"]
        elif "sum" in text:
            steps = ["extract_numbers", "sum", "summarize"]
        elif "max" in text:
            steps = ["extract_numbers", "max"]
        elif "min" in text:
            steps = ["extract_numbers", "min"]

    return steps


# ✅ Execution engine (with validation fix)
def run_agent(query):
    steps = plan_steps(query)

    # ✅ Ensure extract_numbers is always present for math tasks
    if any(step in steps for step in ["sum", "average", "max", "min"]):
        if "extract_numbers" not in steps:
            steps.insert(0, "extract_numbers")

    data = None
    result = None
    outputs = []

    for i, step in enumerate(steps, 1):

        if step == "extract_numbers":
            data = extract_numbers(query)
            outputs.append(f"[Step {i}] Extracted numbers: {data}")

        elif step == "sum":
            result = calculate_sum(data)
            outputs.append(f"[Step {i}] Sum: {result}")

        elif step == "average":
            result = calculate_average(data)
            outputs.append(f"[Step {i}] Average: {result}")

        elif step == "max":
            result = find_max(data)
            outputs.append(f"[Step {i}] Max: {result}")

        elif step == "min":
            result = find_min(data)
            outputs.append(f"[Step {i}] Min: {result}")

        elif step == "summarize":
            summary = summarize_result(result)
            outputs.append(f"[Step {i}] Summary: {summary}")

    return steps, outputs