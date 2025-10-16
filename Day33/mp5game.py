import random

# Rock, Paper, Scissors Game

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Get user choice
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Get computer choice
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

# Determine winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You Win! 🎉")
    else:
        print("You Lose! 😢")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You Win! 🎉")
    else:
        print("You Lose! 😢")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You Win! 🎉")
    else:
        print("You Lose! 😢")
else:
    print("Invalid choice! Please enter rock, paper, or scissors.")
