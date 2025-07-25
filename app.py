from todo import add_task, list_tasks, complete_task, delete_task
from db import init_db

init_db()

def menu():
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            tasks = list_tasks()
            for task in tasks:
                status = "✔" if task[2] else "✘"
                print(f"{task[0]}. {task[1]} [{status}]")
        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
