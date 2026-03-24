import random
num = random.randint(1,100)
tries = 0
print("Welcome to number guessing game")

while True:
    guess = int(input("Enter your number between 1 and 100 : "))
    if num == guess:
        tries += 1
        print(f"you are right! you guessed the number in {tries} tries")
        break
    elif num > guess:
        tries += 1
        print("go a little higher")
 
    elif num < guess:
        tries += 1
        print("go a little lower")
        
    else:
        tries += 1
        print("invalid input")
