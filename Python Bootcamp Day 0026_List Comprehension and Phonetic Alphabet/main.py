import random
#List comprehension - create new list from current list
    #would currently do this via loop and list.append()

#list comprehension pseudo code below
#new_list = [new_item for item in list]
import random

import pandas

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#instead w/ list comprehension -

new_list2 = [n+1 for n in numbers]
#new_list = [new_item for item in list] ^
print(new_list2)

name = "gravytas"
letter_list = [x for x in name]
print(letter_list)

number_list = [x*2 for x in range(1,5)]
print(number_list)

#conditional list comprehension
#new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [x for x in names if len(x)<5]
print(short_names)

long_names = [name.upper() for name in names if len(name)>4]
print(long_names)

#PRACTICE WITH LIST COMPREHENSION
#Exercise 1 - square each number in numbers2 list
numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [num**2 for num in numbers2]
print(squared_nums)

#Exercise 2 - create new list with only even numbers from numbers2
evens = [num for num in numbers2 if num%2==0]
print(evens)

#Exercise 3 - pull numbers from file1.txt and file2.txt and dedupe into one list
with open("./Scripts/file1.txt") as file1:
    data1 = file1.readlines()
    data1_list = [x.strip() for x in data1]
    print(data1_list)

with open("./Scripts/file2.txt") as file2:
    data2 = file2.readlines()
    data2_list = [x.strip() for x in data2]
    print(data2_list)

duplicates = [int(x) for x in data1_list if x in data2_list]
print(duplicates)

###Dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict2 = {new_key:new_value for (key, value) in dict.items()}
# new_dict3 = {new_key:new_value for (key, value) in dict.items() if test}

name = {'Tom', 'Beth', 'Chloe', 'Jake', 'James'}
student_scores = {student:random.randint(1,100) for student in name}
print(student_scores)

#pull students with grade over 60 from created dict above
passed_students = {student:score for (student,score) in student_scores.items() if score>=60}
print(passed_students)

#practice with dictionary compression; count number of letters in each word and create dictionary

import re
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
wordList = re.sub("[^\w]", " ", sentence).split()

result = {word:len(word) for word in wordList}
print(result)

#take each temp in celsius and convert to farenheit
weather_c = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 14,
    "friday": 21,
    "saturday": 22,
    "sunday": 24
}
weather_f = {day:round((temp * (9/5) +32),1) for (day,temp) in weather_c.items()}
print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 99]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

#loop through data frame
for (key,value) in student_dataframe.items():
    print(value)

#loop through rows of dataframe
for (index, row) in student_dataframe.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)



#Challenge
#1 create a dictionary in this format: {"A":"alpha", "B":"bravo", ...}
data5 = pandas.read_csv("phonetic.csv")
phon_dict = {row.Letter:row.Word for (index,row) in data5.iterrows()}

#2 create a list of the phonetic words used for a given words
word = input("Choose a word to create a code: ").upper()
code_output = [phon_dict[letter] for letter in word]
print(code_output)