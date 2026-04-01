def log_step(user_input, tool, output):
    print("\n[LOG]")
    print(f"Input: {user_input}")
    print(f"Tool Selected: {tool}")
    print(f"Output: {output}")
    print("-" * 30)