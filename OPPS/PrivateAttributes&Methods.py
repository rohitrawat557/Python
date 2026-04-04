# Public Attributes and Methods
class Factory:
    __a = "pune"

    def show(self):
        print(Factory.__a) 

 

obj = Factory()

obj.show()

# class Demo:
#     def __init__(self):
#         self.name = "Public Member"
#         self._age = 21
#         self.__salary = 50000

#     def show(self):
#         print("Inside the class : ")
#         print("Public:", self.name)
#         print("Protected:", self._age)
#         print("Private: ", self.__salary)

# obj = Demo()
# obj.show()