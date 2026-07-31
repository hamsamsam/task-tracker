# Task Tracker
# Hangsam Nembang
# This program gets task details from user and utilises loops

#global variable stores version of the program
program_version:float = 1.0


#Task class
class Task:
    name:str = ''
    priority:str = ''
    time_estimate:int = 0
    urgent:str = ''
    status:bool = False
    cost:float = 0.0
    
    #getter 
    #get title of task, if none is added name the task as untitled which means no title was added
    def get_task_input(self):
        """Gets input for task name and sets default value if not provided

        Returns:
            str:temp_name: name of the task
        """
        temp_name = input("Enter Task Name (Enter 'quit' to exit): ")
        if temp_name == '':
            temp_name = 'untitled'
        return temp_name
        
    def get_priority_input(self):
        """Gets input for priority type

        Returns:
            str: level of priority 
        """
        return input("Enter Task Priority: ")
        
    #conditional to check the priority collects string and returns a message based on it 
    def PriorityMessage(self, priority:str):
        """Generates priority message to return based on the priority status as input

        Args:
            priority (str): priority of task
        """
        if(priority.lower() == 'high'):
            return(f"This {self.name} task is high priority and should be done first")
        elif(priority.lower() == 'medium'):
            return(f"This {self.name} task should be scheduled soon")
        elif(priority.lower() == 'low'):
            return(f"This {self.name} task should be done when time allows")
        else:
            return("Priority input was not recognised. Pease enter a valid priority.")

#print greeting for the user
def greet_user():
    """
    Greet the user no inputs
    """
    print('Welcome to Task Tracker Priority Checker!')
    print()
    input("Press 'Enter' to continue.")
    print()
    
         
#run the program in a while loop
def run_tracker():
    greet_user()

    new_task = Task()

    while True:
        
        new_task.name = new_task.get_task_input()
        if(new_task.name.lower() == 'quit'):
            print("Session Closed. Thank you for using Task Traker.")
            break
        #if the input is not empty, the != checks if the input doesnt equal empty string to proceeed
        elif(new_task.name != ''):
            new_task.priority = new_task.get_priority_input()
            print(new_task.PriorityMessage(new_task.priority))
        else:
            print("Error invalid input.")
   

    
run_tracker()






    
    
