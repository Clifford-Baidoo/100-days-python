import pandas

data = pandas.read_csv("Day 25/226 weather-data.csv")

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
#print(temp_list)

#First solution
#Using the normal way
average = sum(temp_list) / len(temp_list)
#print(average)
    
#Second Solution
#Using the .mean() method in panda
average = data["temp"].mean()
#print(average)

maxi = data["temp"].max()
#print(maxi)

#Get Data in Row
print(data[data.day == "Monday"])

max_temp = data[data.temp == data.temp.max()]
print(max_temp)

print(max_temp.condition)

#Converting Celcius to Fahrenheit
day = data[data.day == "Monday"]
temperature = day.temp

F = (temperature * 9/5) + 32
print(F)

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores" : [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Day 25/227 new_data.csv")
