#define a class
class User():
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        #can set default value
        self.followers = 0
        self.following = 0

    #self parameter passed by default so the method understands what is calling it
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
#end of class definition

user_1 = User("0001", "Tom")
user_2 = User("0002", "Harry")

print(user_1.following)
print(user_2.followers)
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)


#constructor: part of class that initializes the object/instance

class Car():
    #special function to initialize the object/instance; this function will be called everytime an object is
    #"constructed" from this class
    def __init__(self):
        #set attributes
        self.seats = 5
        self.airbags = True

    #define new method (function associated with a class) for the class
    def enter_race_mode(self):
        self.seats = 2




