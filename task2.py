
TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
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
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f'Task "{removed}" removed successfully!\n')
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")
def main():
    tasks = load_tasks()
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

if __name__ == "__main__":
    main()
