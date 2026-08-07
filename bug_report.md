# Bug Report

Description: Task numbers shown in view don't match the index used by complete and delete, causing the wrong task to be affected.

Steps to Reproduce:

Run task_manager.py
Choose add, create a task called "Buy groceries"
Choose add, create a second task called "Walk dog"
Choose view — output shows "1. Buy groceries" and "2. Walk dog"
Choose complete, enter 1 (the number shown for "Buy groceries")

Expected Behavior: The task shown as "1. Buy groceries" is marked complete.

Actual Behavior: Because view_task() displays tasks starting at 1 (i+1) but complete_task()/delete_task() use the number entered as a raw 0-based list index, entering 1 actually marks "Walk dog" (the second task, index 1) complete instead of "Buy groceries" (index 0).

BUG-02

Description: complete_task() has no internal check for an out-of-range index, unlike delete_task(), which does validate.

Steps to Reproduce:

Run task_manager.py
Choose add, create one task
Choose complete
Enter an index that doesn't exist, e.g. 99

Expected Behavior: Program prints an error message like "Error: Invalid task index." and returns to the menu, matching the behavior of delete_task().

Actual Behavior: run_manager() happens to check 0 <= index < len(tasks) before calling complete_task(), so the crash doesn't currently surface through the menu — but complete_task() itself has no such check. If it's ever called without that outside validation (e.g. reused elsewhere or the check is removed), it will raise an unhandled IndexError and crash the program instead of printing a friendly error.
