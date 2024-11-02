with open ('Day 26/file1.txt','r') as file1:
    file_1 = file1.readlines()

with open ('Day 26/file2.txt') as file2:
    file_2 = file2.readlines()

result = [int(number) for number in file_1 if number in file_2 ]
print(result)

 