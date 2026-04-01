from input_handler import get_input
from decision_engine import decide_intent
import actions

def run_agent():
    while True:
        user_input = get_input()
        intent = decide_intent(user_input)

        if intent == "greet":
            print(actions.greet())

        elif intent == "date":
            print(actions.get_date())

        elif intent == "calculate":
            expression = user_input.replace("calculate", "")
            print(actions.calculate(expression))

        else:
            print("Sorry, I don't understand.")

if __name__ == "__main__":
    run_agent()