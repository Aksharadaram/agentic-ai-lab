# tools.py

import re

def extract_numbers(text):
    numbers = list(map(int, re.findall(r'\d+', text)))
    return numbers

def calculate_sum(numbers):
    return sum(numbers) if numbers else "No numbers found"

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else "No numbers found"

def find_max(numbers):
    return max(numbers) if numbers else "No numbers found"

def find_min(numbers):
    return min(numbers) if numbers else "No numbers found"

def summarize_result(result):
    return f"The result is {result}, which represents the computed value."