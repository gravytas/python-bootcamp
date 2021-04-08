#can inherit methods and attributes from other classes for convenience

#Fish class inherits from animal class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        #anything in the animal class is initialized into the 'Fish' class
        super().__init__()

    def breathe(self):
        #pulls in animal breathe() method code
        super().breathe()
        #effectively super imposes new code over the Animal 'breathe()' method
        print("doing this underwater.")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()

#inherited method and attribute from Animal class
nemo.breathe()
print(nemo.num_eyes)
