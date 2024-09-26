
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.\n")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")
        print()

def complete_task():
    view_tasks()  
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def menu():
    while True:
        print("Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
