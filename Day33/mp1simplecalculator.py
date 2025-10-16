# Simple Calculator Program

# Taking input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

# Performing operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
elif operator == '%':
    result = num1 % num2
else:
    print("Invalid operator!")
    result = None

# Display result
if result is not None:
    print(f"Result: {result}")
