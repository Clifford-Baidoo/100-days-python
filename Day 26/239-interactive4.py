sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
wordlist = sentence.split()
print(wordlist)

result = {word:len(word) for word in wordlist}

print(result)
