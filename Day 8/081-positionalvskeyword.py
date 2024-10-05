#Positional Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Clifford Baidoo", "Cape Coast")

#Keyword Arguments
def greet_me(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_me(location="Cape Coast",name="Clifford Baidoo")