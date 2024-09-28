#Number Manipulation and fstrings
#round() function
print(round(8/3))
print(round(8/3,2))
print(round(2.666666,2))

#floor division
print(8//3)
print(type(8//3))

#[operator]= operation
result = 4 / 2
result /= 2
print(result)

score = 0
#user scores a point
score += 1
print(score)

#user loses a point
score -= 1
print(score)

#fstrings
score = 0
height = 1.8
isWinning = True

print(f"your score is {score},your height is {height}, you are winning is {isWinning}")