# logger.py

def log(input_text, steps, outputs):
    with open("logs.txt", "a") as f:
        f.write(f"INPUT: {input_text}\n")
        f.write(f"STEPS: {steps}\n")
        f.write("OUTPUT:\n")
        for out in outputs:
            f.write(out + "\n")
        f.write("-" * 40 + "\n")