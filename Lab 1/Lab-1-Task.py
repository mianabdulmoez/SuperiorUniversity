tasks = list(input("Please Enter Your Tasks"))

def add_task(description):
    task = {"id": len(tasks) + 1, "description": description, "status": "Pending"}
    tasks.append(task)
    print(f"Task added: {description}")

def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for task in tasks:
            print(f"{task['id']}. {task['description']} - {task['status']}")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "Completed"
            print(f"Task {task_id} marked as complete.")
            break
    else:
        print("Task not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted.")

def menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice, please try again.")
