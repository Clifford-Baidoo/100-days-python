# with open("Day 25/226 weather-data.csv") as weather:
#     weather_list = weather.readlines()

#     print(weather_list)

# import csv

# with open("Day 25/226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("Day 25/226 weather-data.csv")
print(data["temp"]) 

