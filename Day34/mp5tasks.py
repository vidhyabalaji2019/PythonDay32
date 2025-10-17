#Task 1
print("Task 1:")
for char in "PYTHON":
    print(char)

#Task 2
print("Task 2:")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

# Task 3 Reverse a string using a for loop
print("Task 3:")
text = input("Enter a string: ")
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text
print("Reversed string:", reversed_text)

#Task 4 Print numbers from 1 to 20 using range()
print("Task 4:")
for i in range(1, 21):
    print(i)

#Task 5 Print even numbers from 2 to 50
print("Task 5:")
for i in range(2, 51, 2):
    print(i)

#Task 6 Print numbers in reverse order from 10 to 1
print("Task 6:")
for i in range(10, 0, -1):
    print(i)

#Task 7 Ask user for numbers until they enter 0 (break)
print("Task 7:")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print("You entered:", num)

#Task 8 Skip multiples of 5 from 1 to 50 (continue)
print("Task 8:")
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)

#Task 9 Use pass when number is 5
print("Task 9:")
for i in range(1, 11):
    if i == 5:
        pass  # Do nothing for 5
    else:
        print(i)

#Task 10 After loop ends, print “Loop finished successfully”
print("Task 10:")
for i in range(1, 11):
    print(i)
else:
    print("Loop finished successfully")

#Task 11 Print each character of "HELLO" with index (enumerate)
print("Task 11:")
for index, ch in enumerate("HELLO"):
    print(f"Index {index}: {ch}")

#Task 12 Print each word with position using enumerate()
print("Task 12:")
sentence = input("Enter a sentence: ")
words = sentence.split()
for index, word in enumerate(words, start=1):
    print(f"Word {index}: {word}")

#Task 13 Multiplication table (1 to 10) using nested loop
print("Task 13:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)

#Task 14 Infinite loop printing “Hello, World!”
print("Task 14:")
while True:
    print("Hello, World!")

#Task 15 Stop infinite loop after 5 seconds
print("Task 15:")
import time

start_time = time.time()
while True:
    print("Hello, World!")
    if time.time() - start_time > 5:
        break

#Task 16 Infinite input loop, break on “exit”
print("Task 16:")
while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break
    print("You entered:", user_input)

#Task 17 Print even numbers from 1 to 20 using while + continue
print("Task 17:")
num = 1
while num <= 20:
    num += 1
    if num % 2 != 0:
        continue
    print(num)

#Task 18 Ask for positive number only
print("Task 18:")
while True:
    num = int(input("Enter a positive number: "))
    if num < 0:
        print("Negative number ignored.")
        continue
    print("Thank you! You entered:", num)
    break

#Task 19 Print all numbers except multiples of 3 (1–30)
print("Task 19:")
num = 1
while num <= 30:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1

#Task 20 Number guessing game (1–10)
print("Task 20:")
import random
secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("🎉 Correct guess!")
        break
    else:
        print("❌ Try again!")

#Task 21 Password verification loop
print("Task 21:")
correct_password = "python123"

while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("✅ Access Granted")
        break
    else:
        print("❌ Wrong password. Try again.")

#Task 22 ATM PIN with 3 attempts
print("Task 22:")
correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("✅ Access Granted!")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN! {attempts} attempts left.")
        if attempts == 0:
            print("🚫 Account Locked")

#Task 23 Loop 10 times but do nothing (pass)
print("Task 23:")
for i in range(10):
    pass

#Task 24 Placeholder loop with pass
print("Task 24:")
for i in range(5):
    pass  # TODO: Implement logic later

#Task 25 While loop with else (1 to 5)
print("Task 25:")
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully")

#Task 26 Break loop on “Python”, else message
print("Task 26:")
while True:
    word = input("Enter a word: ")
    if word == "Python":
        print("You entered Python! Loop stopped.")
        break
else:
    print("You never entered 'Python'!")