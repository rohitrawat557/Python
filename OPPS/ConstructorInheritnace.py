class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    pass
 
 
animal1 = Animal("Lion")
person1 = Human("Rohit")

animal1.show()
person1.show()