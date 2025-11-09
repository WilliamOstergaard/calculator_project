import math
from operations import *
print("Welcome to WILLY CALC!")
print("Current possible calculations:")
print("+, -, * , /, ^, sqrt()")
print("All follow PEMDAS")
print("")

def calculation(expression):
    #Checks if there are sqrt()s in expression
    while 'sqrt(' in expression:
        start = expression.find('sqrt(')
        end = expression.find(')',start)
        
        inner = expression[start+5:end]
        
        inner_result = calculation(inner) ** 0.5
        
        expression = expression[:start] + str(inner_result) + expression[end+1:]

    #Checks if there are () in expression, NOT including sqrt()
    while '(' in expression:
        start_parenth = expression.rfind('(')
        end_parenth = expression.find(')', start_parenth)

        inner = expression[start_parenth+1:end_parenth]

        inner_result = calculation(inner)

        expression = expression[:start_parenth] + str(inner_result) + expression[end_parenth+1:]
    
    numbers_list = []
    operators_list = []
    current_number = ""

    #Checks operators in expression
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        
        elif char in ['+','-','*','/','^']:
            operator = char
            num_as_float = float(current_number)
            numbers_list.append(num_as_float)
            current_number = ""
            operators_list.append(operator)
    num_as_float = float(current_number)
    numbers_list.append(num_as_float)


    #Calculates in order of PEMDAS

    i = 0

    while i < len(operators_list):
        num1 = numbers_list[i]
        num2 = numbers_list[i+1]
        if operators_list[i] == '^':
            current_calc = pow(num1,num2)
            numbers_list[i] = current_calc
            numbers_list.pop(i+1)
            operators_list.pop(i)
        elif operators_list[i] == "*":
            current_calc = mult(num1,num2)
            numbers_list[i] = current_calc
            numbers_list.pop(i+1)
            operators_list.pop(i)
        elif operators_list[i] == "/":
            current_calc = div(num1,num2)
            if current_calc == "Error! Division by zero.":
                print("Not possible to divide with 0!")
                exit()
            numbers_list[i] = current_calc
            numbers_list.pop(i+1)
            operators_list.pop(i)
        else:
            i += 1

    i = 0
    while i < len(operators_list):
        num1 = numbers_list[i]
        num2 = numbers_list[i+1]
        if operators_list[i] == '+':
            current_calc = add(num1,num2)
            numbers_list[i] = current_calc
            numbers_list.pop(i+1)
            operators_list.pop(i)
        elif operators_list[i] == "-":
            current_calc = sub(num1,num2)
            numbers_list[i] = current_calc
            numbers_list.pop(i+1)
            operators_list.pop(i)
        else:
            i += 1
    return numbers_list[0]

#Quitting Calculator, and else returns results
while True: 
    user_input = input("Enter calculation: (or type 'quit' or 'q' to exit) ")
    if user_input.lower() in ['quit','q','exit']:
        print("Goodbye!")
        break
    result = calculation(user_input)
    print(f"Result: {result}")
    print("")