# Assignment 1: Rule-Based AI Agent

## Objective

To build a simple AI agent using rule-based logic that processes user input, identifies intent, and performs corresponding actions.

---

## Architecture

```text
Input → Decision → Action
```

This assignment implements a **monolithic agent**, where decision-making and execution are tightly coupled.

---

### 1. Input Handler

* Takes user input
* Normalizes it (lowercase, removes extra spaces)

### 2. Decision Engine

* Uses keyword matching to determine user intent
* Maps input to predefined intents like:

  * greet
  * date
  * calculate

### 3. Actions

* Each action is implemented as a function:

  * Greeting response
  * Current date retrieval
  * Arithmetic calculation

### 4. Agent (Controller)

* Coordinates the flow:

  * Takes input
  * Determines intent
  * Executes corresponding action

---

## Key Features

* Continuous interaction using a loop
* Basic intent recognition using rules
* Simple arithmetic evaluation
* Structured but single-file implementation

---

## Example Usage

```
Enter command: hello
Hello! How can I help you?

Enter command: date
2026-04-01

Enter command: calculate 5 + 3
8
```

---

## Limitations

* Relies on exact keyword matching
* Cannot understand natural language variations
* Decision and execution are tightly coupled
* Uses `eval()` which is not safe for real-world applications

---

## Learning Outcomes

* Understanding of basic agent architecture
* Implementation of input → decision → action pipeline
* Importance of separating logical components
* Awareness of limitations of rule-based systems

---

## Conclusion

This assignment demonstrates a foundational AI agent design.
However, the tight coupling between decision and execution limits scalability, motivating the need for tool abstraction in the next assignment.
