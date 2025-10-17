# Mini Project 8: To-Do List Manager
# Features: Add, View, Remove tasks, and Exit

tasks = []  # List to store tasks

print("📝 Welcome to the To-Do List Manager!")
print("Available commands: add, view, remove, exit")

while True:
    command = input("\nEnter a command: ").lower()

    if command == "add":
        task = input("Enter a new task: ").strip()
        if task == "":
            print("⚠️ Task cannot be empty!")
            continue
        tasks.append(task)
        print(f"✅ Task '{task}' added successfully!")

    elif command == "view":
        if not tasks:
            print("📭 No tasks in your list.")
        else:
            print("\n🗒️ Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif command == "remove":
        if not tasks:
            print("⚠️ No tasks to remove!")
            continue
        try:
            task_no = int(input("Enter the task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                print(f"🗑️ Task '{removed_task}' removed successfully!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif command == "exit":
        print("👋 Exiting the To-Do List Manager...")
        break

    else:
        print("❓ Invalid command! Please use add, view, remove, or exit.")

else:
    # This block runs only if the loop ends naturally (not by 'break')
    print("✅ Program completed successfully without early exit.")
