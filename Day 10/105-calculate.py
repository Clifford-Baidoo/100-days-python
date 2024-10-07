#Calculator
from art import logo
#Adding
def add(n1, n2):
    return n1 + n2

#Subtracting
def sub(n1, n2):
    return n1 - n2

#Multiplication
def mult(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

operators = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
            }


def calc():
    print(logo)
    num1 = float(input("What's the first number: "))
    for i in operators:
        print(i)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number: "))
        calculate = operators[operation_symbol]
        answer = calculate(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type y to continue calculating with {answer} or a to start a new calculation or n to stop calculating: ")
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            if choice == "a":
                calc()
            else:
                print("Goodbye")

calc()