#Using dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

#retrieve items from dictionary
#print(programming_dictionary["Function"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

#create empty dictionary
#empty_dictionary = {}

#wipe existing dictionary
#programming_dictionary = {}

#edit item in dictionary
#programming_dictionary["Bug"] = "methed out butterflies"

#loop through keys in a dictionary
for x in programming_dictionary:
  print(x)

#loop through values in a dictionary
for key in programming_dictionary:
  print(programming_dictionary[key])

#nesting dictionaries
capitals = {
  "France" : "Paris",
  "Lithuania" : "Vilnius"
}  

#nesting a list in a dictionary
travel_log = {
  "USA" : ["Indianapolis", "Dallas", "Denver", "Memphis"],
  "Lithuania" : ["Kaunas", "Vilnius"],
  "England" : "London"
}

#nesting a dictionary in a dictionary
travel_log2 = {
  "USA" : {"Cities visited": ["New York City", "Pensacola", "Austin", "Jacksonville"]},
  "Lithuania" : {"Cities visited": ["Kaunas", "Vilnius"], "times visited" : 1},
  "England" : "London"
}

#nesting a dictionary in a list
travel_log3 = [
  {
    "country" : "USA", 
    "cities_visited": ["Las Vegas", "Detroit", "Chicago"], 
    "total visits": "dozens"
    },
  {
    "country" : "Lithuania", 
    "cities_visited" : ["Kaunas", "Vilnius"], 
    "total_visits" : 1
    },
  {
    "country" : "England", 
    "cities_visited" : "London", 
    "times_visited  : 1"}
]