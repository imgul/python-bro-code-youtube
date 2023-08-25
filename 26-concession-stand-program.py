menu = {
    "pizza": 3.41,
    "burger": 2.00,
    "shawarma": 1.0,
    "soda": 4.20,
    "mint": 3.02,
    "lemonade": 3.32
}

cart = []
total = 0

print("------------ Menu -----------")
for food, price in menu.items():
    print(f"{food.upper():10}: {price:.2f}")
print("-----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()

    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- Your Order --------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total Amount: ${total:.2f}")
