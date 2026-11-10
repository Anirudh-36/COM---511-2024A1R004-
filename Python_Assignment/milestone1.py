# Milestone 1 - Basic data handling and bill calculation
# MIET Campus Canteen Ordering and Billing System

print("===== MIET CAMPUS CANTEEN - SINGLE ITEM BILL =====")

# a) Accept the order details 
student_name = input("Enter student name: ")
item_name = input("Enter item name: ")

# b) Convert numeric inputs to suitable data types
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price (Rs.): "))
gst_percent = float(input("Enter GST percentage: "))

print()
print("Data type of quantity   :", type(quantity))
print("Data type of unit price :", type(unit_price))

# c) Arithmetic operators for the bill
subtotal = quantity * unit_price
gst_amount = subtotal * gst_percent / 100
final_amount = subtotal + gst_amount

# d) String operation: title() capitalises each word neatly
print()
print("Student :", student_name.title())
print("Item    :", item_name.title())
print(f"Subtotal     : Rs. {subtotal:.2f}")
print(f"GST ({gst_percent}%)   : Rs. {gst_amount:.2f}")
print(f"Final Amount : Rs. {final_amount:.2f}")
