from input_handler import get_input
from planner import create_plan
from executor import execute_plan

def run_agent():
    while True:
        user_input = get_input()

        plan = create_plan(user_input)

        if not plan:
            print("No plan could be created.")
            continue

        print("\n[PLAN]")
        for step in plan:
            print(step)

        result = execute_plan(plan, user_input)

        print("\nFinal Output:", result)


if __name__ == "__main__":
    run_agent()