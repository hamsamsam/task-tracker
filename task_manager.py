#a global list of tasks 
tasks = []


def add_task(name, priority, estimated_time):
    """Add task to the tasks list

    Args:
        name (str): name of program
        priority (str): priority level
        estimated_time (int): _description_
    """
    new_task = {
        "name": name,
        "priority": priority,
        "is_complete": False,
        "estimated_time": estimated_time
    }
    
    tasks.append(new_task)
    

def view_task():
    """Prints out entire task lists
    """
    for i, task in enumerate(tasks):
        print(f"{i}. {task["name"]} | Priority: {task["priority"]} | Status: {task["is_complete"]} | Est. Time: {task["estimated_time"]}")
    

def complete_task(index):
    """mark task as complete

    Args:
        index (int): index of task to change
    """
    tasks(index)["is_complete"] = True
    print(f"Task marked complete: {tasks(index)["name"]}")
    
    
def delete_task(index):
    """delete a user selected task from the list 

    Args:
        index (int): index of task to delete
    """
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Error: Invalid task index.")
