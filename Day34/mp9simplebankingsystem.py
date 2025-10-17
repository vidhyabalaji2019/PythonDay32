# Mini Project 9: Simple Banking System

balance = 10000  # Initial account balance
print("🏦 Welcome to the Simple Banking System!")
print("Available commands: deposit, withdraw, balance, quit")

while True:
    command = input("\nEnter a command: ").lower()

    if command == "deposit":
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("⚠️ Please enter a valid amount greater than 0.")
                continue
            balance += amount
            print(f"✅ ₹{amount} deposited successfully!")
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")
            continue

    elif command == "withdraw":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("⚠️ Please enter a valid amount greater than 0.")
                continue
            elif amount > balance:
                print("❌ Insufficient balance!")
                continue
            balance -= amount
            print(f"💰 ₹{amount} withdrawn successfully!")
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")
            continue

    elif command == "balance":
        print(f"📊 Current Balance: ₹{balance}")

    elif command == "quit":
        print("👋 Thank you for using the Simple Banking System!")
        break  # Exit the loop

    else:
        print("❓ Invalid command! Please use deposit, withdraw, balance, or quit.")
        pass  # Placeholder for any future feature

else:
    # This executes only if loop ends naturally (without 'break')
    print("✅ Banking session completed successfully.")
