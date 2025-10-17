# Mini Project 4: Number Guessing Game

import random

# Randomly select a secret number between 1 and 20
secret_number = random.randint(1, 20)
attempts = 5

# Game loop
while attempts > 0:
    guess = int(input("Guess a number between 1 and 20: "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break  # Exit the loop when guessed correctly
    elif guess > secret_number:
        print("📉 Too high! Try again.")
    else:
        print("📈 Too low! Try again.")
    
    # Decrease remaining attempts
    attempts -= 1
    
    if attempts == 0:
        print(f"❌ Out of attempts! The correct number was {secret_number}.")
    else:
        pass  # Placeholder for future enhancements
