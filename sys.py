import sys

def add (num1,num2):
    addition = num1 + num2
    return addition

def sub(num1,num2):
    subtraction = num1 - num2
    return subtraction

def mul(num1,num2):
    multiplication = num1 * num2
    return multiplication

def div(num1,num2):
    try:
        division = num1 / num2
        return division
    except ZeroDivisionError:
        return "Number can't be divisble by zero"

    

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation in ["add", "addition", "+" ]:
    output = add(num1,num2)
    print("addition of " + str(num1) + " and " + str(num2) + " is  :  " + str(output) + "\n")

if operation in ["sub", "subtraction", "-" ]:
    output = sub(num1,num2)
    print("subtraction of " + str(num1) + " and " + str(num2) + " is  :  " + str(output) + "\n")

if operation in ["mul", "multiplication", "*" ]:
    output = mul(num1,num2)
    print("multiplication of " + str(num1) + " and " + str(num2) + " is  :  " + str(output) + "\n")

if operation in ["div", "division", "/" ]:
    output = div(num1,num2)
    print("division of " + str(num1) + " and " + str(num2) + " is  :  " + str(output) + "\n")

