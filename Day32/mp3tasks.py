# Task 1: Print Your Name
print("Task 1:Print Your Name")
print("Vidhya")

# Task 2: Print Multiple 
print("Task 2:Print Multiple")
print("Welcome to Python Programming!\nLet's learn and grow together.")

# Task 3: Variable Assignment
name = "Vidhya"
age = 21
favorite_color = "Blue"
print("Task 3:Variable Assignment")
print("Name:", name)
print("Age:", age)
print("Favorite Color:", favorite_color)

# Task 4: Data Type Identification
a = "Hello"     # string
b = 25          # integer
c = 45.67       # float
d = True        # boolean
print("Task 4:Data Type Identification")
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Task 5: Taking User Input
name = input("Enter your name: ")
print("Task 5:Taking User Input")
print(f"Welcome, {name}!")

# Task 6: Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Task 6:Sum of Two Numbers")
print(f"The sum of {num1} and {num2} is {total}")


# Task 7: Data Type Conversion
print("Task 7:Data Type Conversion")
num = input("Enter a number: ")
print("Before conversion:", type(num))
num = float(num)
print("After conversion:", type(num))


# Task 8: Formatted Sentence Using f-Strings
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("Task 8:Formatted Sentence Using f-Strings")
print(f"Hello {name}, you are {age} years old and live in {city}.")


# Task 9: Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("Task 9:Area of a Rectangle")
print(f"The area of the rectangle is {area:.2f} square units.")


# Task 10: Printing a Receipt
item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = quantity * price
print("Task 10:Printing a Receipt")
print("\n===== RECEIPT =====")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price:.2f}")
print(f"Total: ${total:.2f}")
print("===================")


# Task 11: Swap Two Variables
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a
print("Task 11:Swap Two Variables")
print(f"After swapping: a = {a}, b = {b}")


# Task 12: Temperature Converter
print("Task 12:Temperature Converter")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")


# Task 13: Simple Profile Display
print("Task 13:Simple Profile Display")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in cm): "))
hobby = input("Enter your favorite hobby: ")

print("\n===== User Profile =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} cm")
print(f"Favorite Hobby: {hobby}")
print("========================")
