menu={
    'Fried Rice':50,
    'Biriyani':90,
    'Chicken Lolipop':20,
    'Chowmin':70,
    'Egg-Roll':35,
}
print("Welcome to PYTHON Restaurant")
print("Fried Rice:50\nBiriyani:90\nChicken Lolipop:20\nChowmin:70\nEgg-Roll:35")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet")

print(f"The total amount of items to pay is {order_total}")
