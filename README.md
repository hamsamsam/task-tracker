# task-tracker

Week 9 Day 3

# Task Tracker

Hangsam Nembang
Task tracker used to add/delete tasks to lists.

## Project Structure

- task_input.py: Collects basic task information from the user using variables and input/output.
- task_priority.py: Adds priority logic using conditionals and a while loop.
- task_tracker.py: Refactored version using functions, scope, and docstrings.
- task_manager.py: Implements the task manager using a list of task dictionaries with features to add, view, complete, and delete tasks.
- data_model.md: Documents the task data model, including the task dictionary structure, requirements mapping, and data model assumptions.

## Reflection

- What problem did adding file persistence solve?
  Adding file persistence solved the issue of the list of tasks being wiped after each time the program executes. This allows the user to come
  back to the task at another date.
- What would happen to the Task Manager if you did not catch the FileNotFoundError when loading tasks?
  If the FileNotFoundError was not caught the program would crash.
- How does error handling connect to the QA mindset from Week 1 Day 4?
  Error handling connects to the QA mindset by identifying and managing unexpected situations that would cause the program to fail. By preparing for a file not found error it prevents the program from crashing if the file is missing.
