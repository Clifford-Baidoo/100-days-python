#This will give you a type error
#num_char = len(input("What is your name?"))
#print("Your name has" + num_char + "characters.")

num_char = len(input("What is your name?"))
print(type(num_char))

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has" + new_num_char + "characters.")

a = 123
print(type(a)) 

a = str(123)
a = float(123)

print(70 + float("100.5"))