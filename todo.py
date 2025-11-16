import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the text file into a list."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks


def save_tasks(tasks):
    """Save the list of tasks to the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")
    print("===========================")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Invalid task. Please try again.")


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting... Your tasks have been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
