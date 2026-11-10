"""canteen_utils.py - helper functions for the MIET Campus Canteen application."""
import time

MENU = {"Burger": 80, "Sandwich": 60, "Juice": 40, "Coffee": 30}

def calculate_subtotal(items, menu=MENU):
    """Return the total price of an items dictionary {item: quantity}."""
    subtotal = 0
    for item, quantity in items.items():
        subtotal += menu[item] * quantity
    return subtotal

def calculate_discount(subtotal, threshold=300, rate=0.10):
    """Return the discount amount (default: 10% on bills of Rs. 300 or more)."""
    if subtotal >= threshold:
        return subtotal * rate
    return 0.0

def get_timestamp():
    """Return the current date and time using the standard time module."""
    return time.strftime("%d-%m-%Y %H:%M:%S")

def generate_bill(order_id, student_name, items, menu=MENU,
                  canteen_name="MIET Campus Canteen"):
    """Build the complete bill as a printable string."""
    subtotal = calculate_subtotal(items, menu)
    discount = calculate_discount(subtotal)
    final_amount = subtotal - discount

    line = "=" * 42
    rows = [line, canteen_name.center(42), line,
            f"Order ID : {order_id}",
            f"Student  : {student_name}",
            f"Time     : {get_timestamp()}",
            "-" * 42,
            f"{'Item':<12}{'Qty':>5}{'Price':>11}{'Amount':>12}"]
    for item, quantity in items.items():
        price = menu[item]
        rows.append(f"{item:<12}{quantity:>5}{price:>11.2f}{price * quantity:>12.2f}")
    rows += ["-" * 42,
             f"{'Subtotal':<26}Rs. {subtotal:>9.2f}",
             f"{'Discount':<26}Rs. {discount:>9.2f}",
             f"{'Final Amount':<26}Rs. {final_amount:>9.2f}",
             line]
    return "\n".join(rows)
