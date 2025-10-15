
print("*" * 40)
print("\t✨ Welcome to FreshMart ✨")
print("*" * 40)
print("        123 Main Street, Chennai")
print("        Contact: +91 98765 43210")
print("*" * 40)

# Items Section
print("Item\t\tQty\tPrice (₹)")
print("-" * 40)
print("Tomatoes\t1kg\t₹40.00")
print("Potatoes\t2kg\t₹60.00")
print("Rice\t\t5kg\t₹250.00")
print("Oil\t\t1L\t₹160.00")
print("-" * 40)

# Calculations
subtotal = 40 + 60 + 250 + 160
tax = subtotal * 0.05  # 5% tax
total = subtotal + tax

# Totals Section
print(f"Subtotal:\t\t₹{subtotal:.2f}")
print(f"Tax (5%):\t\t₹{tax:.2f}")
print("=" * 40)
print(f"TOTAL:\t\t\t₹{total:.2f}")
print("=" * 40)

# Footer Section
print("\t💚 Thank You for Shopping! 💚")
print("\t   Visit Again Soon 😊")
print("=" * 40)
