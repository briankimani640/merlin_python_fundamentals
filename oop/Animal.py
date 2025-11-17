class Animal: #Parent class
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def speak(self,sound):
        return f"{sound}"

# classes defined using nameofclass() -> this class is observing inheritance
class Lion(Animal): #sub classes
    # use super method to add attributes that are not in the inherited scope
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age
    def eat(self):
        return f"{self.name} eats Meat!!"

class Cub(Lion):
    def __init__(self, name, breed, age, dob):
        super().__init__(name, breed, age)
        self.dob = dob

class Cat(Animal): # sub classes
    def eat(self):
        return f"{self.name} eats Meat and drinks Milk!!"
    # method overriding - define the method same way but gives diffrentaction
    def speak(self, sound):
        return f"{self.name} makes a sound {sound}"
    
lion = Lion("Simba", "BreedA", 10)
cat = Cat("Moon", "CatX")
print(f"{lion.eat()} and makes the sound {lion.speak('roars')}")
print (lion.speak("roar")) # polymorphism
print (cat.speak("meows"))


# Classes can inherit from multipl parent classes: simply seperate them with a , (comma)
# Method Resolutio Order: simply observes priority to the class on the left
class A:
    def greet(self):
        return "Hello from A"
    
class B:
    def greet(self):
        return "Hello from B"
    
class C(B,A):
    pass

object_c = C()
print (object_c.greet())
