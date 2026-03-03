# Ducktyping =  another way to achieve polymorphism besides inheritance
#               Object must have the min necessary attributes/methods
# "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

def print_name(obj):
    print(obj.name)          # we only care that .name exists

class Person:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name
 
class Car:
    def __init__(self):
        self.name = "Tesla Model S"

p = Person("Rohit")
d = Dog("Bruno")
c = Car()

print_name(p)      # works
print_name(d)      # works
print_name(c)      # also works!