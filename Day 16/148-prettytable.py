from prettytable import PrettyTable


#TODO: Challenge 1 - Create an object under the pretty table class and name it as table
table = PrettyTable()
#TODO: Challenge 2 - Add two colums to the table and give it any data you want
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
#TODO: Challenge 3 - Aligns the items in the list for it to be left aligned
table.align = "l"
print(table)