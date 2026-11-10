# main.py - MIET Campus Canteen Ordering and Billing System (final version)
import canteen_utils
import canteen_storage
from canteen_order import CanteenOrder

def show_menu():
    print("\n========== CANTEEN MENU ==========")
    for item, price in canteen_utils.MENU.items():
        print(f"{item:<10} Rs. {price:.2f}")
    print("==================================")
def take_order():
    student_name = input("Enter student name: ").strip().title()
    order = CanteenOrder(canteen_storage.next_order_id(), student_name)
    show_menu()

    while True:
        entry = input("Enter item name (or DONE to finish): ").strip()
        if entry.upper() == "DONE":
            break
        item = entry.title()
        if item not in canteen_utils.MENU:
            print(f"Sorry, '{item}' is not available. Please choose from the menu.")
            continue
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError("quantity must be greater than zero")
        except ValueError as error:                      # invalid numeric input
            print(f"Invalid quantity ({error}). Please enter a whole number.")
            continue
        order.add_item(item, quantity)

    if not order.items:
        print("No items were ordered. Order cancelled.")
        return
    print()
    order.display_bill()
    canteen_storage.save_order(order)
    print(f"Order #{order.order_id} saved to {canteen_storage.FILENAME}")

def view_orders():
    try:
        records = canteen_storage.read_orders()
    except FileNotFoundError:                            # file not created yet
        print(f"No saved orders found: '{canteen_storage.FILENAME}' does not exist yet.")
        return
    print("\n------------ SAVED ORDERS ------------")
    for record in records:
        order_id, student, items, total, when = record.split("|")
        print(f"Order #{order_id} | {student} | {items} | Rs. {total} | {when}")
    print(f"Total orders saved: {len(records)}")

def update_price():
    item = input("Enter item whose price changes: ").strip().title()
    if item not in canteen_utils.MENU:
        print(f"Sorry, '{item}' is not on the menu.")
        return
    try:
        new_price = float(input("Enter new price (Rs.): "))
        if new_price <= 0:
            raise ValueError("price must be greater than zero")
    except ValueError as error:                          # invalid numeric input
        print(f"Invalid price ({error}). Price not changed.")
        return
    canteen_utils.MENU[item] = new_price
    print(f"{item} price updated to Rs. {new_price:.2f}")

def main():
    print("===== MIET CAMPUS CANTEEN ORDERING AND BILLING SYSTEM =====")
    while True:
        print("\n1. New order\n2. View saved orders\n3. Update item price\n4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            take_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            update_price()
        elif choice == "4":
                print("Thank you for using the canteen system.")
                break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
