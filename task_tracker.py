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
    
    #print greeting for the user
    def greet_user():
        print(""""
            Task Tracker
            
            An app to track your tasks.
            
            """
        )
        input("Press 'Enter' to continue.")
    
      
    #conditional to check the priority
    def PriorityMessage(self):
        if(self.priority.lower() == 'high'):
            print("This task is high priority and should be done first")
        elif(self.priority.lower() == 'medium'):
            print("This task should be scheduled soon")
        elif(self.priority.lower() == 'low'):
            print("This task should be done when time allows")
        else:
            print("Priority input was not recognised. Pease enter a valid priority.")
    
        
    
#welcome message

usr_input = ''
#get input from user about task while the user does not quit
while True:
    print("Enter Task Name (Enter 'quit' to exit)")
    usr_input = input()
    if(usr_input.lower() == 'quit'):
        print("Session Closed. Thank you for using Task Traker.")
        break
    #if the input is not empty, the != checks if the input doesnt equal empty string to proceeed
    elif(usr_input != ''):
        new_task = Task()
        new_task.name = usr_input
        print("Enter Task Priority")
        new_task.priority = input("->")
        new_task.PriorityMessage()
    else:
        print("Error invalid input.")
   






    
    
