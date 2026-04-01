a = int(input("Enter a number : "))
# a = input("Enter a number : ")

try:
    print(10/a)

except Exception as e:
    print(f"Sorry there is an error as {e}")

else:
    print("Good there is no exception")


print("Ok i have done the division")