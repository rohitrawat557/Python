try: 
    number = int(input("Enter a number : "))
    print(1/number)
except ZeroDivisionError:
    print("you cannot divide by zero!")
except ValueError:
    print("Enter only number please!")
except Exception:
    print("Something went wrong!")
finally:
    print("This will always execute!")