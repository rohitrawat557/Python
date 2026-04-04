# Public Attributes and Methods
class Factory:
    _a = "pune"

    def _show(self):
        print("Hello I am a pune Factory")

class Bhopal(Factory):
    def show2(self):
        print(super()._a)

obj = Bhopal()
obj._show()
obj.show2()