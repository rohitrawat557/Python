age = int(input("Enter your age : "))
try:
    if age < 10 or age > 18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("welcome to the club")
except Exception as e:
    print(f"an Error occured as : {e}")


print("The club will start soon")