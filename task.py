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
        self.__priority = priority
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
        self.__priority = priority
        
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
        return(
            f"""
            Name: {self.name}
            Estimated Time: {self.estimated_time}
            Priority: {self.get_priority}
            Status: {self.get_complete} 
            """
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
            task_dict["priority"],
            task_dict["estimated_time"]
        )

        if task_dict.get("is_complete", False):
            task.mark_complete()

        return task
    