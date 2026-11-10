# main.py - Milestone 4: main program that imports the user-defined module
import time
from canteen_utils import calculate_subtotal, calculate_discount, MENU
from canteen_order import CanteenOrder
order = CanteenOrder(101, "Aman")
order.add_item("Burger", 3)
order.add_item("Coffee", 2)

# The items dictionary is passed to a function in canteen_utils
subtotal = calculate_subtotal(order.items)
print("Subtotal                        : Rs.", subtotal)
print("Discount (default 300 / 10%)    : Rs.", calculate_discount(subtotal))
print("Discount (keyword 200 / 5%)     : Rs.",
      calculate_discount(subtotal, threshold=200, rate=0.05))

# Bill-generation time using the standard time module
print("Bill generated on:", time.strftime("%A, %d %B %Y at %H:%M:%S"))
print()
order.display_bill()
