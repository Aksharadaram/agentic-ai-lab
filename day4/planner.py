def create_plan(user_input):
    user_input = user_input.lower()

    plan = []

    # Example: average + summarize
    if "average" in user_input and "summarize" in user_input:
        plan.append({
            "step": "extract_numbers",
            "action": "extract_numbers"
        })
        plan.append({
            "step": "calculate_average",
            "action": "calculate_average"
        })
        plan.append({
            "step": "summarize_result",
            "action": "summarize"
        })

    return plan