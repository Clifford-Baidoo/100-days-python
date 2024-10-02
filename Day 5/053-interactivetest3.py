#Adding Evens
#You are going to write a program that calculates the sum of all the even numbers from 1 to 100,including 1 and 100
#e.g 2 + 4 + 6 + 8 + 10 + ... + 98 + 100

#Solution 1
even =  0
for number in range(1,101):
    if number % 2 == 0:
        even += number

print(even)

#Solution 2
total = 0
for number in range(2,101,2):
    total += number

print(total)