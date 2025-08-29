#Create a class "Pets" from a class "Animals" and further create a class "Dogs" from the class "Pets". Add a method bark() in the class Dogs which prints "Woof Woof".

class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    def bark(self):
        print("Woof Woof")

dog = Dogs()
dog.bark()