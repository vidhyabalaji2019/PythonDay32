# Mini Project 2: Number Pyramid Generator

# Take input from the user
rows = int(input("Enter number of rows for the pyramid: "))

# Check for invalid input
if rows < 0:
    print("Invalid input. Exiting...")
else:
    # Generate pyramid pattern
    for i in range(1, rows + 1):
        if i % 2 == 0:
            continue  # Skip even rows
        for j in range(i):
            print(i, end=" ")
        print()  # Move to next line
