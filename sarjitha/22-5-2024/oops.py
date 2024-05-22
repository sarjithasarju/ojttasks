class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def description(self):
        return f"{self.name} is {self.age} years old"

  
    def speak(self, sound):
        return f"{self.name} says {sound}"


dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)


print(dog1.species)  


print(dog1.name)  
print(dog2.age)   


print(dog1.description()) 
print(dog2.speak("Woof"))  
