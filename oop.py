class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello my name is", self.name)


person1 = person("Tomilola", 15)
person1.greet()

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} says woof!"

Dog1 = Dog("Jason", "German shepherd")
Dog1.bark()