## Day 25 - Working with CSV Files and Analysing Data with Pandas

### 225 - Day 25 Goals
We are going to use a library called Pandas
We will be building a guessing game about all the states in US
### 226 - Reading CSV Data in Python

A CSV, or Comma-Separated Values file, is a simple text format used to store tabular data, such as spreadsheets or databases. Each line in a CSV file represents a row of data, and within each row, values are separated by commas. 

For Example:
```Python
Name,Age,Occupation
Alice,30,Engineer
Bob,25,Designer

```

There is a spreadsheet with the days of the week,temperature and condition
We are going to use it to learn how to read CSV

#Challenge
Open the weather_data.csv
User .readlines() to create a list named data that contains the values of the .csv file.

#Check 266-csv.py for solution

We are going import the csv librabry that helps with CSVs
Then we will open up our weather file and use the csv.reader funtion to read the csv file and seperate the data intoe rows

```Python
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
```

#Challenge
Create a new list called Temperatures which will add the temperatures in the weather.csv file

#Solution
Check 266-csv.py

We are going to use the Pandas library which is a python data analysis library

To start you have to install the pandas library
and also read the [documentation](pandas.pydata.org/docs/)
```Python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

print(data["temp"])

```

So we imported panda and used the read function to open the file and read it 
And to get a specific column all we have to do is specify te column name

### 277 - DataFrames & Series_Working with Rows and Columns

A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure commonly used in data analysis and manipulation, particularly with the Pandas library in Python. 
It resembles a spreadsheet or a SQL table, where data is organized in rows and columns.

A Series is a one-dimensional labeled array in Pandas, which can hold any data type, such as integers, floats, strings, or even Python objects. 
It's similar to a column in a DataFrame but can also be thought of as a list with associated labels.

When you go to the API reference page you can see all the things you can do with pandas
And you can see the DataFrame and Series section
Check it out and see how it can be used

```Python
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
```

#Challenge
Calculate the average temperature
Solution is in 227-DataFrame.py

#Challenge
After checking the soulution
Use one of the Panda series methods to find the maximum value in temperatures
Solution is in 227-DataFrame.py

#Getting Rows in the DataFrame
To do that we will go into the column and check for the row where the value is equal to a value in the colum

```python
print(data[data.day == "Monday"])

#To get a specific value in a row
Monday = data[data.day == "Monday"]
print(Monday.condition)
```
The data.day is the same as data["day"] it is just another way to use a column
and we can get a specific value of row by doing the same thing we do to a DataFrame but in the row

#Challenge
Print the row of data which had the highest temperature

#Challenge
Convert Monday's temperature to Fahrenheit
#Solution Check 277-DataFrame.py for solution

#Create a dataframe from scratch

Let's say we already have a dictionary and we want to turn it into a dataframe

```Python
data_dict = {
    "students": ["Amy","James","Angela"]
    "scores" : [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
```
We call our pandas library and call our DataFrame class and add the dictionary name to the Data Frame class
You can also save it into a csv file by using the to_csv() method

### 288 - The Great Squirrel Census Data Analysis
We are going to analyze the squirrel census made in America
The CSV file will be in the folder

#Challenge
Get the sum of the black squirrels , do same for grey and cinnamon
When you are done create a new data frame for them 

#Solution
Check 228-squirrel.py for solution

### 299 U.S. States Game_Part 1_Setup
A zip file has been given to you
It contains 3 files , a gif,main.py and a csv file
Go online and check what the States Game is
We are basically going to recreate it
Check how it works [game](https://www.sporcle.com/games/g/states)

You can try making it on your own or heading to the final solution to get the solution

### 301 - Congratulations
YOu have completed day 25 Congrats