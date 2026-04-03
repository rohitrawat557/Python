class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your object details are material: {self.material},  zips: {self.zips}, pockets: {self.pockets}")


reebok = Factory("leather", 2, 4)

campus = Factory("nylon",3,3)

reebok.show()
campus.show()