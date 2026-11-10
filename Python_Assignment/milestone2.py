# milestone.py - Milestone 1 extended with Milestone 2 (menu, decisions and loops)

# Kept from Milestone 1: accept the student name
student_name = input("Enter student name: ")

# a) The fixed menu is stored in a dictionary (item name -> price)
menu = {"Burger": 80, "Sandwich": 60, "Juice": 40, "Coffee": 30}
order = {}          # selected items -> quantity

print("\n========== CANTEEN MENU ==========")
for item, price in menu.items():
    print(f"{item:<10} Rs. {price}")
print("==================================")

# b) Keep accepting items until the user types DONE
while True:
    entry = input("Enter item name (or DONE to finish): ").strip()
    if entry.upper() == "DONE":
        break
    item = entry.title()

    # c) Selection statement: reject items that are not on the menu
    if item in menu:
        quantity = int(input("Enter quantity: "))
        order[item] = order.get(item, 0) + quantity      # d) store the order
    else:
        print("Sorry, this item is not available. Please choose from the menu.")

# d) Calculate the total bill
print("\n------------- BILL -------------")
print("Student :", student_name.title())      # kept from Milestone 1 (string operation)
print("--------------------------------")
total = 0
for item, quantity in order.items():
    amount = menu[item] * quantity
    print(f"{item:<10} {quantity:>3} x {menu[item]:>3} = Rs. {amount:>7.2f}")
    total += amount

# e) 10% discount for bills of Rs. 300 or more
if total >= 300:
    discount = total * 0.10
else:
    discount = 0
final_amount = total - discount

print("--------------------------------")
print(f"Total      : Rs. {total:.2f}")
print(f"Discount   : Rs. {discount:.2f}")
print(f"Final Bill : Rs. {final_amount:.2f}")
