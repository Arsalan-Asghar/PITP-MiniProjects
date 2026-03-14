# Week 3 - 1. Mini-Project 1 - To-Do List Manager:

import json

TODO_FILE = "todo_list.json"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"pending": [], "completed": []}

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def todo_manager():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            tasks["pending"].append(task)
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == "2":
            print("\nTasks:")
            for task in tasks["pending"]:
                print(f"- {task}")
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

todo_manager()