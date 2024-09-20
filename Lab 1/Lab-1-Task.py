import json
from datetime import datetime

try:
    with open('todo_list.json', 'r') as file:
        todo_list = json.load(file)
except FileNotFoundError:
    todo_list = []

def save_todo_list():
    with open('todo_list.json', 'w') as file:
        json.dump(todo_list, file, indent=4)

def add_task(description, priority, due_date, assigned_to, category, notes, dependencies):
    task = {
        'Task Description': description,
        'Priority': priority,
        'Due Date': due_date,
        'Status': 'Not Started',
        'Assigned To': assigned_to,
        'Category': category,
        'Notes': notes,
        'Dependencies': dependencies,
        'Progress': 0
    }
    todo_list.append(task)
    save_todo_list()

def update_status(task_index, status):
    todo_list[task_index]['Status'] = status
    save_todo_list()

def update_progress(task_index, progress):
    todo_list[task_index]['Progress'] = progress
    save_todo_list()

def check_overdue_tasks():
    current_date = datetime.now().strftime('%Y-%m-%d')
    for task in todo_list:
        if task['Due Date'] < current_date and task['Status'] != 'Completed':
            task['Status'] = 'Overdue'
    save_todo_list()

def filter_tasks(filter_type, filter_value):
    filtered_tasks = [task for task in todo_list if task[filter_type] == filter_value]
    return filtered_tasks

def display_todo_list(tasks=None):
    if tasks is None:
        tasks = todo_list
    for index, task in enumerate(tasks):
        print(f"Task {index + 1}: {task['Task Description']}")
        print(f"Priority: {task['Priority']}")
        print(f"Due Date: {task['Due Date']}")
        print(f"Status: {task['Status']}")
        print(f"Assigned To: {task['Assigned To']}")
        print(f"Category: {task['Category']}")
        print(f"Notes: {task['Notes']}")
        print(f"Dependencies: {task['Dependencies']}")
        print(f"Progress: {task['Progress']}%")
        print("-" * 40)

def main():
    check_overdue_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. Update task status")
        print("3. Update task progress")
        print("4. Display to-do list")
        print("5. Filter tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            assigned_to = input("Enter assigned to: ")
            category = input("Enter category: ")
            notes = input("Enter any notes: ")
            dependencies = input("Enter dependencies: ")
            add_task(description, priority, due_date, assigned_to, category, notes, dependencies)
            print("Task added successfully!")
        elif choice == '2':
            task_index = int(input("Enter task number to update status: ")) - 1
            status = input("Enter new status (Not Started/In Progress/Completed): ")
            update_status(task_index, status)
            print("Task status updated successfully!")
        elif choice == '3':
            task_index = int(input("Enter task number to update progress: ")) - 1
            progress = int(input("Enter new progress percentage (0-100): "))
            update_progress(task_index, progress)
            print("Task progress updated successfully!")
        elif choice == '4':
            display_todo_list()
        elif choice == '5':
            filter_type = input("Filter by (Priority/Status/Category): ")
            filter_value = input(f"Enter the {filter_type} to filter by: ")
            filtered_tasks = filter_tasks(filter_type, filter_value)
            display_todo_list(filtered_tasks)
        elif choice == '6':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()