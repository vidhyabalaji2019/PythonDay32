# Discount Calculator Program

# Taking user input
bill = float(input("Enter your total bill amount: ₹"))

# Applying discount based on rules
if bill >= 5000:
    discount = bill * 0.20
elif bill >= 3000:
    discount = bill * 0.10
elif bill >= 1000:
    discount = bill * 0.05
else:
    discount = 0.0

# Calculating final amount
final_amount = bill - discount

# Displaying result
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Bill Amount: ₹{final_amount:.2f}")
