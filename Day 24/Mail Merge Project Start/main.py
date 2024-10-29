#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()

with open("Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

    for name in names_list:
        name = name.strip()
        new_letter = letter_contents.replace("[name]", name)
        with open(f"/home/mee_pmeep/Documents/Python_Yu_Project/Day 24/Mail Merge Project Start/Output/ReadyToSend/letter for {name}.txt",mode="w") as n_letter:
            n_letter.write(new_letter)