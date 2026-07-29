# Task Tracker
# Hangsam Nembang
# This program gets task details from user

#Task class
class Task:
    name:str = ''
    priority:str = ''
    time_estimate:int = 0
    urgent:str = ''
    status:bool = False
    cost:float = 0.0
    
    def PrintSummary(self):
        print("====================")
        print("Task Summary")
        print("====================")
        print("")
        print("Task Name: ",self.name)
        print("Task Priority: ",self.priority)
        print("Task Time Estimate: ",self.time_estimate)
        print("Urgency: ",self.urgent)
        print("")
        
        
        
    
#welcome message
print(""""
      Task Tracker
      
      An app to track your tasks.
      
      """
)

input("Press 'Enter' to continue.")

#get input from user about task 
new_task = Task()
print("Enter Task Name")
new_task.name = input("->")
print("Enter Task Priority")
new_task.priority = input("->")
print("Enter Task Time Estimate")
new_task.time_estimate = int(input("->"))
print("Is task urgent yes/no?")
new_task.urgent = input("->")

new_task.PrintSummary()





    
    
