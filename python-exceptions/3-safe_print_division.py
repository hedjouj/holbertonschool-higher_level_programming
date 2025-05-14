#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero!")