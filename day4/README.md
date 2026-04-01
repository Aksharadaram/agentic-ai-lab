"# Day 4" 
# Assignment 4: Multi-Step Planning Agent

## Objective

To build an agent capable of solving multi-step problems through planning.

---

## Architecture

```
Input → Planner → Step-wise Execution → Final Output
```

---

## Components

* `planner.py` → Breaks task into steps
* `executor.py` → Executes each step sequentially
* `tools.py` → Reused tools
* `agent.py` → Controls workflow

---

## Example Workflow

Input:

```
Find the average of 5, 10, 15 and summarize the result
```

Execution:

1. Extract numbers
2. Calculate average
3. Summarize result

---

## Key Features

* Task decomposition
* Sequential execution
* Shared context between steps
* Intermediate output display

---

## Key Improvement Over Assignment 3

* Supports multi-step reasoning
* Introduces planning layer
* Enables complex task handling

---

## Limitations

* Hardcoded planning logic
* Limited task coverage

---

## Learning Outcome

* Planning-based agents
* Context management
* Sequential reasoning systems
