"# Day 2" 
# Assignment 2: Tool-Using Agent

## Objective

To design an agent that can use external tools dynamically.

---

## Architecture

```
Input → Decision → Tool Selection → Execution
```

---

## Components

* `tools.py` → Defines reusable tools
* `decision_engine.py` → Selects appropriate tool
* `agent.py` → Executes selected tool

---

## Tools Implemented

* Calculator
* Weather (mock)
* Text summarizer

---

## Key Improvement Over Assignment 1

* Separation of decision and execution
* Introduction of tool abstraction
* Improved modularity and scalability

---

## Limitations

* Rule-based tool selection
* Limited natural language handling

---

## Learning Outcome

* Tool abstraction
* Function mapping
* Modular programming design
