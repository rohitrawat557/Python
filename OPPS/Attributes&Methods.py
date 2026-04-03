class Animal:

    def __init__(self,age):
        self.age = age  #instance attribute

    def show(self): #instance method
        print(f"how are you, your age is {self.age}")

    @classmethod
    def classmethod(cls): # this methods target the class and not the instance
        print("this is a class method")

    @staticmethod
    def static():  # this method is not related to the class or the instance its just a method that is realted to the class
        print("this is a static method")

obj = Animal(12)
obj.show()
Animal.classmethod()
obj.static()