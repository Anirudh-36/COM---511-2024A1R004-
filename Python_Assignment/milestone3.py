# milestone.py - Milestone 3: the same application refactored using OOP

# from Milestone 2: the menu stored in a dictionary
menu = {"Burger": 80, "Sandwich": 60, "Juice": 40, "Coffee": 30}

class CanteenOrder:
    canteen_name = "MIET Campus Canteen"        # a) class variable (shared by all orders)

    def __init__(self, order_id, student_name):  # b) constructor
        self.order_id = order_id
        self.student_name = student_name
        self.items = {}                    # item name -> quantity

    # c) instance methods
    def add_item(self, item, quantity):
        if item in menu:                         
            self.items[item] = self.items.get(item, 0) + quantity
            return True
        print(f"Sorry, {item} is not available.")
        return False

    def calculate_total(self):
        subtotal = 0
        for item, quantity in self.items.items():
            subtotal += menu[item] * quantity
        discount = subtotal * 0.10 if subtotal >= 300 else 0    # same 10% rule
        return subtotal, discount, subtotal - discount

    def display_bill(self):
        subtotal, discount, final_amount = self.calculate_total()
        print("=" * 42)
        print(CanteenOrder.canteen_name.center(42))
        print("=" * 42)
        print(f"Order ID : {self.order_id}")
        print(f"Student  : {self.student_name}")
        print("-" * 42)
        for item, quantity in self.items.items():
            print(f"{item:<12}{quantity:>5} x {menu[item]:>3} = {menu[item] * quantity:>9.2f}")
        print("-" * 42)
        print(f"Subtotal     : Rs. {subtotal:.2f}")
        print(f"Discount     : Rs. {discount:.2f}")
        print(f"Final Amount : Rs. {final_amount:.2f}")
        print("=" * 42)

    def __str__(self):                     # d) short order summary
        total_qty = sum(self.items.values())
        return (f"Order #{self.order_id} | {self.student_name} | "
                f"{total_qty} item(s) | Rs. {self.calculate_total()[2]:.2f}")

# e) Create two order objects and display their bills
order1 = CanteenOrder(101, "Aman")
order1.add_item("Burger", 3)
order1.add_item("Coffee", 2)

order2 = CanteenOrder(102, "Riya")
order2.add_item("Juice", 2)
order2.add_item("Sandwich", 1)
order2.add_item("Pasta", 1)     # not on the menu, so it is rejected

order1.display_bill()
print()
order2.display_bill()
print()
print(order1)
print(order2)
