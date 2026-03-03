foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit) : ")
    if food.lower() == "q":       #.lower() → converts whatever the user typed to lowercase
        break
    else:
        price = float(input(f"Enter the price of a {food} :$"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food,end=" ")

for price in prices:
    total += price

print()
print(f"Your total is = ${total}")





# User typed a food and its price → 
#    ↓
# We save them both → 
#    ↓
# Add food name to the foods list    → foods.append(food)
# Add the price number to prices list → prices.append(price)
#    ↓
# Now we "remember" this item forever (until program ends)