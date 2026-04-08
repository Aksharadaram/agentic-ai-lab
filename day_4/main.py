# main.py

from agent import run_agent
from logger import log

while True:
    query = input("Enter query (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Exiting program...")
        break

    steps, outputs = run_agent(query)

    print("\nPlanned Steps:", steps)
    print("\nExecution:")

    for out in outputs:
        print(out)

    log(query, steps, outputs)