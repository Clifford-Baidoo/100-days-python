#Calculator

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

num1 = int(input("What's the first number: "))
for i in operators:
    print(i)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number: "))

calculate = operators[operation_symbol]
answer = calculate(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")