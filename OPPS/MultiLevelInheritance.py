
class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class BhopalFaactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFaactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

    def show(self):
        print(f"Your object details are material: {self.material}, zips: {self.zips}, color: {self.color}, pockets: {self.pockets}")

obj = PuneFactory("Leather", 2, "Black", 4)
obj.show()