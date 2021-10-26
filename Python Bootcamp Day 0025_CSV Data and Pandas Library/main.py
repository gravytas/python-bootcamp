'''
with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)
'''

###practicing use pandas library
import csv
import pandas

'''
###opens csv file
with open("weather_data.csv") as file:

    ###creates data object using csv import with all csv data
    data = csv.reader(file)

    #loop throw rows in newly created object
    for x in data:
        print(x)

    ###create list of temperatures in integer format
    temperatures = []
    for x in data:
        if x[1] != "temp":
            temperatures.append(int(x[1]))
    print(temperatures)

###use pandas to open csv and pull temp
data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print(data)
print(data["temp"])
### whole table data type is a 'data frame'; each column is a 'series' type

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
temp_list2 = data.temp.to_list()
print(temp_list)
print(temp_list2)

###find avg of temps in temp_list
temps = 0
for x in temp_list:
    temps += x
avg = temps/len(temp_list)
print(round(avg,0))

###OR
sum(temp_list)/len(temp_list)
data["temp"].mean()

###find max of temps in temp_list
max = data["temp"].max()
print(max)

#pull column from data object
print(data.condition)

#pull data from rows
print(data[data.day == "Monday"])

#pull row where temp was the maximum
print(data[data.temp == data.temp.max()])

#convert monday temp to farenheit
monday = data[data.day == "Monday"]
mon_cels = monday.temp
mon_far = ((9/5)*mon_cels) +32
print(round(mon_far,0))

###create dataframe from scratch (table)
new_dict = {
    "Students":["Amy", "James", "Tom"],
    "Scores":[75, 50, 68]
}
new_data = pandas.DataFrame(new_dict)
print(new_data)
new_data.to_csv("new_data.csv")
'''

#Challenge - create csv with count of squirrels of each fur color

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_list = squirrel_data["Primary Fur Color"].to_list()
print(squirrel_list)

gray = 0
black = 0
cinnamon = 0

for color in squirrel_list:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

squirrel_color_data = pandas.DataFrame(squirrel_dict)
print(squirrel_color_data)

squirrel_color_data.to_csv("squirrel_color_data.csv")









