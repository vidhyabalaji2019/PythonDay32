# Mini Project 2: Simple Bill Calculator
# AI POWERED PYTHON DJANGO MYSQL LEARNING MATERIAL

# Taking user input
item_name = input("Enter the item name: ")
price = float(input("Enter the price per item: "))
quantity = int(input("Enter the quantity: "))

# Tax rate (10%)
tax_rate = 0.10

# Calculating totals
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# Checking types
print(f"Type of item_name: {type(item_name)}")  # str
print(f"Type of price: {type(price)}")          # float
print(f"Type of quantity: {type(quantity)}")    # int
print(f"Type of total: {type(total)}")          # float

# Printing formatted bill
print("\n===== Bill Summary =====")
print(f"Item: {item_name}")
print(f"Price per item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (10%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")
print("=================================")
print("Thank you for shopping with us!")
