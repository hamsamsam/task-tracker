# Task Tracker
# Hangsam Nembang
# This program gets task details from user and utilises loops

#Task class
class Task:
    name:str = ''
    priority:str = ''
    time_estimate:int = 0
    urgent:str = ''
    status:bool = False
    cost:float = 0.0
    
    #getter 
    def get_task_input(self):
        print("Enter Task Name (Enter 'quit' to exit)")
        return input("->")
        
    def get_priority_input(self):
        print("Enter Task Priority")
        return input("->")
        
    #conditional to check the priority collects string and returns a message based on it 
    def PriorityMessage(self, priority:str):
        if(priority.lower() == 'high'):
            return("This task is high priority and should be done first")
        elif(priority.lower() == 'medium'):
            return("This task should be scheduled soon")
        elif(priority.lower() == 'low'):
            return("This task should be done when time allows")
        else:
            return("Priority input was not recognised. Pease enter a valid priority.")

#print greeting for the user
def greet_user():
    print(""""
        Task Tracker
        
        An app to track your tasks.
        
        """
    )
    input("Press 'Enter' to continue.")
    
         
#run the program
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






    
    
