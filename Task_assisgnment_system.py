assigned_tasks = []

def assign_task():
    user = input("Enter user name: ")
    task = input("Enter task description: ")
    assigned_tasks.append({"user": user, "task": task})
    print("Task assigned successfully")

def view_tasks():
    if not assigned_tasks:
        print("No tasks assigned")
    else:
        for task in assigned_tasks:
            print(task["user"], "- Task:", task["task"])

def main():
    while True:
        print("1. Assign Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            assign_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
