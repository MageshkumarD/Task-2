import os

# File that stores tasks
TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from TASKS_FILE. If the file doesn't exist return an empty list."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []


def save_tasks(tasks):
    """Save the list of tasks to TASKS_FILE."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your To-Do List!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Task "{task}" added successfully!\n')
    else:
        print("Task cannot be empty.\n")


def remove_task(tasks):
    if not tasks:
        print("\nNo tasks to remove.\n")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: ").strip())
    except ValueError:
        print("Please enter a valid number!\n")
        return

    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f'Task "{removed}" removed successfully!\n')
    else:
        print("Invalid task number!\n")


def main():
    tasks = load_tasks()
    try:
        while True:
            print("==== To-Do List Manager ====")
            print("1. View tasks")
            print("2. Add task")
            print("3. Remove task")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                view_tasks(tasks)
            elif choice == "2":
                add_task(tasks)
            elif choice == "3":
                remove_task(tasks)
            elif choice == "4":
                print("Goodbye! Your tasks are saved.")
                break
            else:
                print("Invalid choice! Please enter 1-4.\n")
    except KeyboardInterrupt:
        print("\n\nExiting. Your tasks are saved.")


if __name__ == "__main__":
    main()
