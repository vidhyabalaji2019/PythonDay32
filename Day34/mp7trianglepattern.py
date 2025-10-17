# Mini Project 7: Triangle Pattern Generator

# Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

print("\nTriangle Pattern:")

# Generate the triangle pattern
for i in range(1, rows + 1):
    # Print only odd-numbered rows to match the sample output
    if i % 2 != 0:
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line

print("Triangle generation completed.")
