tasks = []

def add_task():
    task = input("Enter a new task: ")
    priority = input("Set priority (low, medium, high): ").lower()
    if priority not in ["low", "medium", "high"]:
        print("Invalid priority. Defaulting to 'low'.")
        priority = "low"
    tasks.append({"task": task, "completed": False, "priority": priority})
    print(f"Task '{task}' added with priority '{priority}'.\n")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.\n")
    else:
        print("\nYour To-Do List (sorted by priority):")
    
        priority_order = {"high": 1, "medium": 2, "low": 3}
        sorted_tasks = sorted(tasks, key=lambda x: priority_order[x["priority"]])

        counter = 1
        for task in sorted_tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"{counter}. {task['task']} - {status} - Priority: {task['priority'].capitalize()}")
            counter += 1
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