#Average Height Exercise
'''You are going to write a program that calculates the average student height from a List of heights.

e.g student_heights = [180,124,165,173,189,169,146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights'''

#Don't change the code below
student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
#Don't change the code below

#Write your code below
total_height = 0
for height in student_heights:
    total_height += height

num_of_students = 0
for students in student_heights:
    num_of_students += 1

average_height = total_height / num_of_students

print(round(average_height))