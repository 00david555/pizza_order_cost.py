# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Pizza Order Cost Calculator

# 1. Collect user inputs
pizza_size = input("Enter pizza size (small/large): ").lower()
toppings = int(input("Enter number of additional toppings: "))
distance = float(input("Enter delivery distance in miles: "))

# 2. Calculate base pizza price
if pizza_size == "small":
    base_price = 8
elif pizza_size == "large":
    base_price = 12
else:
    print("Invalid pizza size!")
    exit()

# 3. Calculate toppings cost
toppings_cost = toppings * 1

# 4. Calculate delivery fee
if distance == 0:
    delivery_fee = 0
elif distance <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (distance - 5) * 1

# 5. Calculate total cost
total_cost = base_price + toppings_cost + delivery_fee

# 6. Display order summary
print("\n----- ORDER SUMMARY -----")
print(f"Pizza size: {pizza_size}")
print(f"Base price: ${base_price:.2f}")
print(f"Toppings cost: ${toppings_cost:.2f}")
print(f"Delivery fee: ${delivery_fee:.2f}")
print(f"Total cost: ${total_cost:.2f}")
