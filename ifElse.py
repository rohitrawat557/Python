name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are an adult.")
else:
    print(f"Hello {name}, you are not an adult.")
    b = 18-age
    print(f"You can vote in {b} years.")