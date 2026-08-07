# task-tracker

Week 9 Day 3

# Task Tracker

Hangsam Nembang
Task tracker used to add/delete tasks to lists.

Task Tracker is a command-line Python app for managing tasks. It supports adding, viewing, completing, and deleting tasks, including urgent tasks (with a deadline) and recurring tasks (with a repeat frequency).

## How to run

Clone the repo: git clone then cd task-tracker
Make sure Python 3.10+ is installed: python3 --version
Run the program: python3 task_manager.py
Use the menu options (add, add-urgent, add-recurring, view, complete, delete, save, quit) to manage tasks. Tasks auto-save to tasks.json and reload next time you run it.

## Features

Add a task with name, priority, and estimated time
Add an urgent task with a deadline (always high priority)
Add a recurring task with a frequency (e.g. daily, weekly)
View all tasks with priority, time, and status
Mark tasks complete
Reset a recurring task for its next cycle
Delete a task
Save/load tasks from tasks.json
Input validation for priority and numeric fields

## Project Structure

- task.py – Task, UrgentTask, RecurringTask classes and task_from_dict()
- task_manager.py – main menu loop: add, view, complete, delete, save, load
- task_test.py – unittest test suite for the Task classes
- task_input.py – early version collecting task info with basic input/output
- task_priority.py – early version adding priority logic
- task_tracker.py – refactored version using functions and docstrings
- data_model.md – documents the task dictionary structure
- tasks.json – auto-generated file storing saved tasks
- README.md – this file

## Reflection

- What problem did adding file persistence solve?
  Adding file persistence solved the issue of the list of tasks being wiped after each time the program executes. This allows the user to come
  back to the task at another date.
- What would happen to the Task Manager if you did not catch the FileNotFoundError when loading tasks?
  If the FileNotFoundError was not caught the program would crash.
- How does error handling connect to the QA mindset from Week 1 Day 4?
  Error handling connects to the QA mindset by identifying and managing unexpected situations that would cause the program to fail. By preparing for a file not found error it prevents the program from crashing if the file is missing.

## Future Improvements

Add feature to hold multiple lists.
Add an edit feature so a task's details can be changed without deleting and re-adding it.
