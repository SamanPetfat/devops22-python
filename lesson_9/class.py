class Animal:
    def __init__(self, family) -> None:
        self.family = family

class Dog(Animal):
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name
    

class Supermarket:
    def __init__(self,name, street,size) -> None:
        self.name = name
        self.street = street
        self.size = size
    

class Coop:
    def __init__(self, name, street,size,owner)-> None:
        self.name = name
        self.street = street
        self.size = size
        self.owner = owner

if __name__ == "__main__":
    dogclass = Dog(2,"Billy")






