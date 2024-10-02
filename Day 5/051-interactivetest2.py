#Highest Score
'''You are going to write a program that calculates the highest score from a list of scores

e.g students_score = [75,65,89,55,91,64,89]
output - The highest score in the class is: x'''

#Don't change the code below
student_scores = input("Input a list of student scores: ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
#Don't change the code above

#Write your code below this row
highest_number = 0
for number in student_scores:
    if number > highest_number:
        highest_number = number

print(highest_number)