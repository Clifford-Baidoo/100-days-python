#BM1 Calculator Exercisei
#Write a program that calculates the Body Mass Index(BMI) from a 
#users weight and height
#BMI = weight(kg)/height**2(m**2)

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height2 = height ** 2
bmi = weight / height2
print(int(bmi))