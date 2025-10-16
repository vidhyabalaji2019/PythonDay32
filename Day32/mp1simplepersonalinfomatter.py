# Mini Project 1: Simple Personal Info Formatter
# AI POWERED PYTHON DJANGO MYSQL LEARNING MATERIAL

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

# Checking types of entered data
print(f"Type of name: {type(name)}")      # Expected output: <class 'str'>
print(f"Type of age: {type(age)}")        # Expected output: <class 'int'>
print(f"Type of height: {type(height)}")  # Expected output: <class 'float'>

# Displaying formatted user details
print("\n===== Personal Information =====")
print(f"Hello {name}, you are {age} years old and {height} cm tall.")
