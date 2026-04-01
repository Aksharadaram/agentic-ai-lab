from datetime import datetime

def greet():
    return "Hello! How can I help you?"

def get_date():
    return str(datetime.now().date())

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"