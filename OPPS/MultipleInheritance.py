class Animal:
    name1 = "Dog"

class Human:
    name2 = "Rohit"

class Robots( Human,Animal):
    name3 = "Charli123"

obj = Robots()
print(obj.name1)
print(obj.name2)
print(obj.name3)