'''Modify the add function to take an unlimited number of arguments.
Use a loop to sum all the arguments inside the function
Test it out by calling add() to calculate the sum of some arguments'''


def add(*args):
    summary = 0
    for n in args:
        summary += n
    print(summary)
add(1,2,3,4,5,6,7,8,9,10)