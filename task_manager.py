import json
from task import Task, UrgentTask, RecurringTask, task_from_dict

# constant for file name, good for maintainability
TASKS_FILE = "tasks.json"

# a global list of tasks
tasks = []


def add_task(name, priority, estimated_time):
    """Add task to the tasks list

    Args:
        name (str): name of program
        priority (str): priority level
        estimated_time (int): _description_
    """
    task = Task(name, priority, estimated_time)
    tasks.append(task)


def add_urgent_task():
    """Prompt the user for details and add a new UrgentTask to the tasks list."""
    name = input("Task name: ")
    deadline = input("Deadline: ")

    try:
        estimated_time = int(input("Estimated time (minutes): "))
        task = UrgentTask(name, estimated_time, deadline)
        tasks.append(task)
        print(f"Urgent task added: {task.name}")

    except ValueError:
        print("Error: Estimated time must be a whole number.")


def add_recurring_task():
    """Prompt the user for details and add a new RecurringTask to the tasks list."""
    name = input("Task name: ")
    priority = input("Priority (Low/Medium/High): ")
    frequency = input("Frequency (e.g. daily, weekly): ")

    try:
        estimated_time = int(input("Estimated time (minutes): "))
        task = RecurringTask(name, priority, estimated_time, frequency)
        tasks.append(task)
        print(f"Recurring task added: {task.name}")

    except ValueError:
        print("Error: Estimated time must be a whole number.")


def view_task():
    """Prints out entire task lists
    """
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def complete_task(index):
    """mark task as complete

    Args:
        index (int): index of task to change
    """
    tasks[index].mark_complete()
    print(f"Task marked complete: {tasks[index].name}")


def delete_task(index):
    """delete a user selected task from the list 

    Args:
        index (int): index of task to delete
    """
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task.name}")
    else:
        print("Error: Invalid task index.")


def save_tasks():
    """save the current list of tasks to a JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

    print("Tasks saved successfully.")


def load_tasks():
    """load tasks from a JSON file."""
    global tasks
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [task_from_dict(t) for t in json.load(file)]

        print(f"Loaded {len(tasks)} task(s).")

    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")


# run manager loop, handles the menu input from user and calls the corresponding functionm
def run_manager():
    """Main loop to call appropriate functions 
    """
    load_tasks()
    print("Welcome to the Task Manager!")
    while True:
        print("Options: add | add-urgent | add-recurring | view | complete | delete | save | quit")
        usr_input = input("-> ").lower()

        if usr_input == "add":
            name = input("Task name: ")
            priority = input("Priority (Low/Medium/High): ")

            try:
                estimated_time = int(input("Estimated time (minutes): "))

                add_task(name, priority, estimated_time)
                save_tasks()
                print("Task added.")

            except ValueError:
                print("Error: Estimated time must be a whole number.")

        elif usr_input == "add-urgent":
            add_urgent_task()
            save_tasks()

        elif usr_input == "add-recurring":
            add_recurring_task()
            save_tasks()

        elif usr_input == "view":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                view_task()

        elif usr_input == "complete":
            try:
                index = int(input("Enter task index: "))

                if 0 <= index < len(tasks):
                    complete_task(index)
                    save_tasks()
                else:
                    print("Error: Invalid task index.")

            except ValueError:
                print("Error: Please enter a valid whole number.")

        elif usr_input == "delete":
            try:
                index = int(input("Enter task index: "))

                delete_task(index)
                save_tasks()

            except ValueError:
                print("Error: Please enter a valid whole number.")
        elif usr_input == "save":
            save_tasks()
            print("File successfully saveadd!")
        elif usr_input == "quit":
            print("Goodbye!")
            save_tasks()
            break

        else:
            print("Invalid option. Please try again.")


run_manager()