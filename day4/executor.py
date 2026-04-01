from tools import TOOLS

def execute_plan(plan, user_input):
    context = {}
    result = None

    for step in plan:
        action = step["action"]

        if action == "extract_numbers":
            numbers = [int(x) for x in user_input.split() if x.isdigit()]
            context["numbers"] = numbers
            print(f"[STEP] Extracted numbers: {numbers}")

        elif action == "calculate_average":
            nums = context.get("numbers", [])
            avg = sum(nums) / len(nums) if nums else 0
            context["average"] = avg
            print(f"[STEP] Average: {avg}")

        elif action == "summarize":
            text = f"The average is {context.get('average')}"
            result = TOOLS["summarize"](text)
            print(f"[STEP] Summary: {result}")

    return result