#Write a program that adds in a 2 digit number e.g if the input was 35,
#then the output should be 3+5 = 8

#solution
#Ask User to input a 2 digit number
number = input("Enter your 2 digit number:\n")
#Get the first and second digits using subscripting then convert string to int
num1 = int(number[0])
num2 = int(number[1])
#Add the two numbers together
sum = num1 + num2
#Print the result
print(sum)