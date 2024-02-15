import argparse

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

def display_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To-Do List Application")
    parser.add_argument("action", choices=["add", "remove", "display"], help="Action to perform")
    parser.add_argument("--task", help="Task description")
    parser.add_argument("--index", type=int, help="Task index")
    args = parser.parse_args()

    if args.action == "add":
        if args.task:
            add_task(args.task)
        else:
            print("Please provide a task description.")
    elif args.action == "remove":
        if args.index is not None:
            remove_task(args.index - 1)
        else:
            print("Please provide a task index.")
    elif args.action == "display":
        display_tasks()
