# Public Attributes and Methods
class Factory:
    a = "pune"

    def show(self):
        print("Hello I am a pune Factory")

class Bhopal(Factory):
    def show2(self):
        print(super().a)

obj = Bhopal()
obj.show()
obj.show2()