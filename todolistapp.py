# To-Do List App

# Task list to store tasks
tasks = []

# Function to display tasks
def show_tasks():
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}, {task}")
    else:
        print("\nNo Tasks yet. Add Some!")

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to remove a task
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed")
    else:
        print("Invalid task number")

# Main loop for user interaction
def main():
    while True:
        print("\nTo-Do List App")
        print("1. Show Tasks")
        print("2. Add Tasks")
        print("3. Remove Tasks")
        print("4. Exit")
    
        choice = input("Enter your choice ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter a new task:")
            add_task(task)
        elif choice == "3":
            show_tasks()
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice == "4":
            print("Exiting the To-Do List App. Gooodbye!")
            break
        else:
            print("invalid choice, please try again")

# Run the app
if __name__ == "__main__":
    main()

#test repo change name