"""canteen_order.py - the CanteenOrder class (Milestone 3, now using canteen_utils)."""
import canteen_utils

class CanteenOrder:
    canteen_name = "MIET Campus Canteen"        # class variable

    def __init__(self, order_id, student_name):
        self.order_id = order_id
        self.student_name = student_name
        self.items = {}                          # item name -> quantity

    def add_item(self, item, quantity):
        """Add an item if it is on the menu; return True/False."""
        if item in canteen_utils.MENU:
            self.items[item] = self.items.get(item, 0) + quantity
            return True
        return False

    def calculate_total(self):
        """Return (subtotal, discount, final_amount)."""
        subtotal = canteen_utils.calculate_subtotal(self.items)
        discount = canteen_utils.calculate_discount(subtotal)
        return subtotal, discount, subtotal - discount

    def display_bill(self):
        print(canteen_utils.generate_bill(self.order_id, self.student_name,
                                          self.items, canteen_utils.MENU,
                                          CanteenOrder.canteen_name))

    def __str__(self):
        total_qty = sum(self.items.values())
        return (f"Order #{self.order_id} | {self.student_name} | "
                f"{total_qty} item(s) | Rs. {self.calculate_total()[2]:.2f}")
