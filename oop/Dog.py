## difine a class using the 'class' keyword
class Dog:
    # initializer -. define the attributes needed for the object
    # __init__(self) -> this allows initialiation of the class attributes 
    # takes in a mandatory parameter called self the other parameters can be the attributes needed
    # self points to the current object in execution
    def __init__(self, name, age, breed): 
        self.name = name
        self.age = age
        self.breed = breed
    
    # object methods -> always pass in self as part of the parameters
    # bark
    def bark(self):
        return f"{self.name} say woof!"
    
## Creating objects from the class
# variable for refrencing the object created
# make a call to the attributeo or method to access
dog1 = Dog("Buddy",3,"Chihuahua")
dog2 = Dog("Rex", 4, "German Shepherd" )
# to access the attributes simply use the dot notation objectname.attriutename
# to access methods simply use the dot notation objectname.method()
print(f"{dog2.name} is a {dog2.breed} and its {dog2.age} years old")
print(dog2.bark())

        
