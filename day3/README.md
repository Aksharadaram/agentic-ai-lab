"# Day 3" 
# Assignment 3: LLM-Based Agent (Simulated)

## Objective

To integrate an LLM-based decision layer for tool selection.

---

## Architecture

```
Input → LLM Decision Layer → Tool Selection → Execution → Logging
```

---

## Components

* `llm_engine.py` → Simulates LLM-based decision making
* `tools.py` → Tool implementations
* `logger.py` → Logs input, tool, and output
* `agent.py` → Main controller

---

## Features

* Simulated intelligent decision making
* Argument extraction from user input
* Logging of agent actions

---

## Important Note

Due to API quota limitations, a simulated LLM approach is used instead of real API calls.
The architecture remains identical to a real LLM-based system.

---

## Key Improvement Over Assignment 2

* Abstract decision layer
* Improved flexibility
* Closer to real-world AI agent design

---

## Limitations

* Heuristic-based logic instead of true AI reasoning
* Limited adaptability

---

## Learning Outcome

* LLM integration concept
* Decision abstraction
* System extensibility
