# Method overriding 
class Animal:
    def show(self):
        print("Hello I am Rohit")

class Human(Animal):
    def show(self):
        print("How are you doing")

obj = Human()
obj.show()