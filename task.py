class Task:
    
    def __init__(self, name:str, priority:str, estimated_time:int):
        """Constructor to create a task object

        Args:
            name (str): name of task
            priority (str): priority of task 
            estimated_time (int): how long in minutes the task will take to complete
        """
        self.name = name
        self.estimated_time = estimated_time
        self.set_priority(priority)
        self.__is_complete = False
        
    
    def get_priority(self):
        """Returns the priority of the task 

        Returns:
            __priority : priority level of the task
        """
        return self.__priority
    
    def set_priority(self, priority:str):
        """Sets the priority of the task 

        Args:
            priority (str): priority level of the task 
        """
        if priority.lower() == 'low' or priority.lower() == 'medium' or priority.lower() == 'high':
            self.__priority = priority
        else:
            print("Error: Invalid priority level, please pick between low/medium/high. Priority set to low as default.")
            self.__priority = 'low'
            
    def get_complete(self):
        """Gets the status of the task 

        Returns:
            bool: returns the status 
        """
        return self.__is_complete
    
    def mark_complete(self):
        """Sets the task status to complete
        """
        self.__is_complete = True
    
    def to_dict(self):
        """returns the value of the object as a dictionary 

        Returns:
            dictionary: dictionary of the object
        """
        return self.__dict__
    
    def to_string(self):
        """
        Docstring to genetrate formatted output 
        
        """
        return(
            f"""
            Name: {self.name}
            Estimated Time: {self.estimated_time}
            Priority: {self.get_priority}
            Status: {self.get_complete} 
            """
        )
        
    def __str__(self):
        """Returns a formatted string representation of the task,
        including name, priority, estimated time, and status.

        Returns:
            str: formatted task details
        """
        status = "Complete" if self.get_complete() else "Pending"
        return (
            f"{self.name} | Priority: {self.get_priority()} "
            f"| Estimated Time: {self.estimated_time} min | Status: {status}"
        )
        
    @classmethod
    def from_dict(cls, task_dict):
        """
        Creates a Task object from a dictionary.

        The dictionary must contain name, priority, and estimated_time.
        If is_complete is True, the new task will be marked as complete.
        """
        task = cls(
            task_dict["name"],
            task_dict["_Task__priority"],
            task_dict["estimated_time"]
        )

        if task_dict.get("_Task__is_complete", False):
            task.mark_complete()

        return task

class UrgentTask(Task):

    def __init__(self, name: str, estimated_time: int, deadline: str):
        """Constructor to create an urgent task, which is always high priority.

        Args:
            name (str): name of task
            estimated_time (int): how long in minutes the task will take to complete
            deadline (str): the deadline by which the task must be completed
        """
        super().__init__(name, "high", estimated_time)
        self.deadline = deadline

    def __str__(self):
        """Returns a formatted string representation of the urgent task,
        including the [URGENT] label and the deadline.

        Returns:
            str: formatted task details
        """
        status = "Complete" if self.get_complete() else "Incomplete"
        return (
            f"[URGENT] {self.name} | Estimated Time: {self.estimated_time} min "
            f"| Status: {status} | Deadline: {self.deadline}"
        )

    def to_dict(self):
        """Returns the urgent task as a dictionary, including its type and deadline.

        Returns:
            dict: dictionary representation of the urgent task
        """
        task_dict = super().to_dict()
        task_dict["type"] = "UrgentTask"
        task_dict["deadline"] = self.deadline
        return task_dict


class RecurringTask(Task):

    def __init__(self, name: str, priority: str, estimated_time: int, frequency: str):
        """Constructor to create a recurring task that repeats on a set frequency.

        Args:
            name (str): name of task
            priority (str): priority level of the task
            estimated_time (int): how long in minutes the task will take to complete
            frequency (str): how often the task recurs (e.g. "daily", "weekly")
        """
        super().__init__(name, priority, estimated_time)
        self.frequency = frequency

    def __str__(self):
        """Returns a formatted string representation of the recurring task,
        including the [RECURRING: frequency] label.

        Returns:
            str: formatted task details
        """
        status = "Complete" if self.get_complete() else "Incomplete"
        return (
            f"[RECURRING: {self.frequency}] {self.name} | Priority: {self.get_priority()} "
            f"| Estimated Time: {self.estimated_time} min | Status: {status}"
        )

    def reset(self):
        """Resets the task's completion status back to False so it can be
        reused in the next cycle.
        """
        self._Task__is_complete = False
        print(f"'{self.name}' has been reset for its next {self.frequency} cycle.")

    def to_dict(self):
        """Returns the recurring task as a dictionary, including its type and frequency.

        Returns:
            dict: dictionary representation of the recurring task
        """
        task_dict = super().to_dict()
        task_dict["type"] = "RecurringTask"
        task_dict["frequency"] = self.frequency
        return task_dict
    
    
def task_from_dict(data):
    """Creates a Task, UrgentTask, or RecurringTask based on the "type" field.

    Args:
        data (dict): dictionary representation of a task

    Returns:
        Task: an instance of Task, UrgentTask, or RecurringTask
    """
    task_type = data.get("type")

    if task_type == "UrgentTask":
        task = UrgentTask(
            data["name"],
            data["estimated_time"],
            data["deadline"]
        )
        if data.get("_Task__is_complete", False):
            task.mark_complete()
        return task

    elif task_type == "RecurringTask":
        task = RecurringTask(
            data["name"],
            data["_Task__priority"],
            data["estimated_time"],
            data["frequency"]
        )
        if data.get("_Task__is_complete", False):
            task.mark_complete()
        return task

    else:
        return Task.from_dict(data)
    
if __name__ == "__main__":
    demo_tasks = [
        Task("Buy groceries", "low", 30),
        UrgentTask("Fix server outage", 5, "2024-12-01"),
        RecurringTask("Team standup", "medium", 15, "daily")
    ]

    print("--- Polymorphism Demo ---")
    for task in demo_tasks:
        print(task)
        print("Is a Task instance:", isinstance(task, Task))
        print()
