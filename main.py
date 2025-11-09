import math
from operations import *
from calculator import calculation

print("Welcome to WILLY CALC!")
print("Current possible calculations:")
print("+, -, * , /, ^, sqrt(), any log")
print("All follow PEMDAS")
print("\nEnter calculation: \n(type 'q' to exit, 'h' for help)\n")


#Sets up calculator, able to quit, help, and return results
while True: 
    user_input = input("")
    if user_input.lower() in ['quit','q','exit']:
        print("Goodbye!")
        break
    if user_input.lower() in ['help', 'h', '?']:
        print("\n=== Available Functions ===")
        print("Basic: +, -, *, /, ^")
        print("sqrt(x) - square root")
        print("log(x) - logarithm base 10")
        print("log2(x) - logarithm base 2")
        print("ln(x) - natural logarithm (base e)")
        print("Use parentheses () for grouping")
        print("==========================\n")
        continue
    result = calculation(user_input)
    print(f"Result: {result:.10g}")
    print("")