'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value

1. Under 18.5 they are underweight
2. Over 18.5 but below 25 they have a normal weight
3. Over 25 but below 30 they are overweight
4. Over 30 but below 35 they are obese
5. Above 35 they are clinically obese'''

#Don't change the code below
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
#Don't change code above

#Write your code below
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} , You are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} , You have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} , You are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f} , You are obese")
else:
    print(f"Your BMI is {bmi:.2f} , You are clinically obese")