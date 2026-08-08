class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal): #This is how inheritance is implemented in Python. The Dog class inherits from the Animal class, which means that it has access to all the methods and attributes of the Animal class.
    def speak(self):
        print("Woof!")

#a=Animal("Dog")
#a.speak()
c=Dog("Buddy")
c.speak()
