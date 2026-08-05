## Section 1: Variables

| Field Name       | Data Type | Description                                                | Default Value |
| ---------------- | --------- | ---------------------------------------------------------- | ------------- |
| `name`           | `str`     | The name or title of the task.                             | User provided |
| `priority`       | `str`     | The priority level of the task (e.g. Low, Medium, High).   | User provided |
| `is_complete`    | `bool`    | Indicates whether the task has been completed.             | `False`       |
| `estimated_time` | `int`     | Estimated time required to complete the task (in minutes). | User provided |

## Section 2: Requirements Mapping

| Functional Requirement                | Data Field or Function              | How It Is Fulfilled                                                                                                                                |
| ------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add a task to the "In Progress" list. | `add_task()`                        | Creates a new task dictionary with the task name, priority, estimated time, and `is_complete` set to `False`, then appends it to the `tasks` list. |
| View a list of active tasks.          | `view_task()`                       | Iterates through the `tasks` list and displays each task's details, including its name, priority, completion status, and estimated time.           |
| Mark a task as completed.             | `complete_task()` and `is_complete` | Updates the selected task's `is_complete` field from `False` to `True` to indicate the task has been completed.                                    |
| Delete a task from all lists.         | `delete_task()`                     | Removes the selected task from the `tasks` list using `pop()`.                                                                                     |

## Section 3: Assumptions

- Tasks are stored only in memory using the global `tasks` list and are lost when the program closes.
- The `estimated_time` value is always entered as a whole number (integer).
- The `priority` value is expected to be one of **Low**, **Medium**, or **High**.
- A completed task is represented by setting the `is_complete` field to `True` rather than moving it to a separate list.
