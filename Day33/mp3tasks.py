# Task 1: Arithmetic Operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Task 1: Arithmetic Operations")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Remainder: {num1 % num2}")



# Task 2: Compare Two Numbers
print("Task 2: Compare Two Numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")


# Task 3: Swap Two Numbers using Arithmetic Operators
print("Task 3: Swap Two Numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")


# Task 4: Check Leap Year
print("Task 4: Check Leap Year")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")


# Task 5: Find Largest Number
print("Task 5: Find Largest Number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the largest.")
elif b >= a and b >= c:
    print(f"{b} is the largest.")
else:
    print(f"{c} is the largest.")


# Task 6: Area of Circle
print("Task 6: Area of Circle")

r = float(input("Enter the radius: "))
area = 3.14 * r * r
print(f"Area of circle: {area}")


# Task 7: Positive, Negative, or Zero
print("Task 7: Positive, Negative or Zero")

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Task 8: Voting Eligibility
print("Task 8: voting Eligibility")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# Task 9: Grade Based on Marks
print("Task 9: Grade Based on Marks")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

    # Task 10: Simple ATM Program
    print("Task 10: Simple ATM Program")

balance = 5000
withdraw = float(input("Enter amount to withdraw: "))

if withdraw > balance:
    print("Insufficient funds.")
else:
    balance -= withdraw
    print(f"Withdrawal successful. Remaining balance: {balance}")


# Task 11: Divisible by 5 and 11
print("Task 11: Divisible by 5 and 11")

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisible by both 5 and 11.")


# Task 12: Vowel or Consonant
print("Task 12: Vowel or Consonant")

ch = input("Enter a character: ").lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")


# Task 13: Even or Odd (Ternary Version)
print("Task 13: Even or Add")

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

