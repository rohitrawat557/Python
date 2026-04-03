
class Factorymumbai:
    a = "I am an attribute mentioned inside factory"
    def hello(self):
        print("hello i am a method mentioned inside factory")

class Factorypune(Factorymumbai):
    pass

obj = Factorymumbai()

obj2 = Factorypune()

obj2.hello()