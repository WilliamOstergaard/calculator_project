import math
from operations import *

def calculation(expression):
    #Library of all possible functions
    functions = {
        'sqrt': lambda x: x ** 0.5,
        'log': lambda x: math.log(x,10),
        'log2': lambda x: math.log(x,2),
        'ln': lambda x: math.log(x),
        'sin': lambda x: math.sin(x),
        'cos': lambda x: math.cos(x),
        'tan': lambda x: math.tan(x)
    }

    for func_name, func in functions.items():
        while f'{func_name}(' in expression:
            start = expression.find(f'{func_name}(')
            end = expression.find(')', start)
            inner = expression[start+len(func_name)+1:end]

            inner_result = func(calculation(inner))

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

    #Checks decimals and operators in expression, splits string-expression based on this
    #converts string numbers to floats
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char == '-' and (not current_number and not numbers_list):
            current_number += char
        elif char == '-' and not current_number and operators_list:
            current_number += char
        elif char in ['+','-','*','/','^']:
            operator = char
            num_as_float = float(current_number)
            numbers_list.append(num_as_float)
            current_number = ""
            operators_list.append(operator)
    num_as_float = float(current_number)
    numbers_list.append(num_as_float)


    #Calculates in order of PEMDAS (EMDAS only)

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
