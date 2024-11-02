import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dict = pandas.read_csv('Day 26/nato_phonetic_alphabet.csv')

phonetics = {row.letter:row.code for (index , row) in dict.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a Word: ").upper()
word_list = [phonetics[letter] for letter in word]

print(word_list)


