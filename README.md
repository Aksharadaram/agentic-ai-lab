# Agentic AI Lab

## Overview

This repository contains a progressive implementation of AI agents, starting from rule-based systems to multi-step planning agents.

The objective is to understand how intelligent agents:

* Interpret user input
* Make decisions
* Use tools
* Execute multi-step tasks

---

## Structure

```
agentic-ai-lab/
│
├── day1/  # Rule-based agent
├── day2/  # Tool-using agent
├── day3/  # LLM-based agent (simulated)
├── day4/  # Multi-step planning agent
```

---

## Assignments Breakdown

### Day 1: Rule-Based Agent

* Implements basic input → decision → action pipeline
* Uses keyword-based intent detection

### Day 2: Tool-Using Agent

* Introduces modular tools
* Agent selects and executes tools dynamically

### Day 3: LLM-Based Agent (Simulated)

* Replaces rule-based decision with simulated LLM logic
* Maintains separation between decision and execution
* Includes logging of agent behavior

### Day 4: Multi-Step Planning Agent

* Introduces planning capability
* Breaks complex tasks into multiple steps
* Executes steps sequentially with shared context

---

## Key Concepts Learned

* Agent Architecture Design
* Tool Abstraction
* Decision vs Execution Separation
* Planning and Task Decomposition
* Modular and Scalable Code Design

---

## Note

Due to API quota limitations, Assignment 3 uses a **simulated LLM decision layer** while preserving the same architecture.

---

## How to Run

Navigate to each folder and run:

```
python agent.py
```

---

## Author

(Your Name)
