def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
        print(f"Saving {len(tasks)} tasks...")

def add_task(tasks):
    task = input("Enter task:")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        num = int(input("Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number.")
        else:
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed}")
    except ValueError:
        print("Please enter a valid number.")

tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "4":
        save_tasks(tasks)
        print("Exiting program...")
        break
        
    elif choice == "1":
        add_task(tasks)
    
    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    else:
        print("invalid input")