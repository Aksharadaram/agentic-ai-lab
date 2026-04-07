from datetime import datetime

# =========================
# INPUT HANDLER
# =========================
def get_input():
    return input("Enter command: ").strip().lower()


# =========================
# DECISION ENGINE
# =========================
def decide_intent(user_input):
    if "hello" in user_input:
        return "greet"
    elif "date" in user_input or "today" in user_input:
        return "date"
    elif "calculate" in user_input:
        return "calculate"
    else:
        return "unknown"


# =========================
# ACTIONS
# =========================
def greet():
    return "Hello! How can I help you?"

def get_date():
    return str(datetime.now().date())

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"


# =========================
# AGENT (CONTROLLER)
# =========================
def run_agent():
    while True:
        user_input = get_input()
        intent = decide_intent(user_input)

        if intent == "greet":
            print(greet())

        elif intent == "date":
            print(get_date())

        elif intent == "calculate":
            expression = user_input.replace("calculate", "").strip()
            print(calculate(expression))

        else:
            print("Sorry, I don't understand.")


# =========================
# MAIN ENTRY
# =========================
if __name__ == "__main__":
    run_agent()