Code Quality

    X All functions and methods have docstrings
    X No unused variables or commented-out code blocks remain in the final files
    X Variable and function names are descriptive and follow Python naming conventions

Correctness

    X Adding a task creates the correct object type and appends it to the list
    X Viewing tasks displays all fields including status
    X Completing a task correctly updates is_complete
    X Deleting a task removes it from the list and prints the correct name
    X Saving writes a valid tasks.json file
    X Loading restores all task types correctly using task_from_dict

Edge Cases

    X The program handles an empty task list gracefully in view_tasks()
    X Invalid priority input is rejected by set_priority()
    X Non-numeric input for estimated time is caught with a ValueError
    X Out-of-range task numbers are handled in complete_task() and delete_task()

Documentation

    X README is complete with all required sections
    X Project Structure section lists every file in the repository
    X Known bugs are documented

Upon reviewing the code with the above checklist, I notices an unused function called "to_string". After checking that the function is not used by task_manager I removed it from the code, reducing the number of unused code.
