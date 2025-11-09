import math
print("Welcome to WILLY CALC!")

user_input = input("Enter calculation: ")

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculation(expression):
    #Checks if there are () in expression
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
        if char.isdigit():
            current_number += char
        
        elif char in ['+','-','*','/','^']:
            operator = char
            num_as_int = int(current_number)
            numbers_list.append(num_as_int)
            current_number = ""
            operators_list.append(operator)
    num_as_int = int(current_number)
    numbers_list.append(num_as_int)


    #Calculates the operations

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

result = calculation(user_input)
print(f"Result: {result}")