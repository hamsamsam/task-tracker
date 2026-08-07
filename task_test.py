import unittest
from task import Task, UrgentTask, RecurringTask

class TestTask(unittest.TestCase):
    def setUp(self):
        """Creates a fresh Task instance before each test."""
        self.NewTask = Task("Buy groceries", "high", 30)
        return super().setUp()

    def test_task_creation(self):
        """Verifies that a newly created Task has the correct name,
        priority, and estimated time.
        """
        self.assertEqual(self.NewTask.name, "Buy groceries")
        self.assertEqual(self.NewTask.get_priority(), "high")
        self.assertEqual(self.NewTask.estimated_time, 30)

    def test_mark_compelte(self):
        """Verifies that mark_complete() sets the task's completion
        status to True.
        """
        self.NewTask.mark_complete()
        self.assertTrue(self.NewTask.get_complete())

    def test_set_priority_invalid(self):
        """Verifies that set_priority() defaults to 'low' when given
        an invalid priority value.
        """
        self.NewTask.set_priority("urgent")
        self.assertEqual(self.NewTask.get_priority(), "low")

    def test_set_priority_valid(self):
        """Verifies that set_priority() correctly sets a valid,
        non-default priority value.
        """
        self.NewTask.set_priority("medium")
        self.assertEqual(self.NewTask.get_priority(), "medium")

    def test_to_dict(self):
        """Verifies that to_dict() returns a dictionary containing
        all expected fields with correct values.
        """
        task_dict = self.NewTask.to_dict()
        self.assertEqual(task_dict["name"], "Buy groceries")
        self.assertEqual(task_dict["estimated_time"], 30)
        self.assertEqual(task_dict["_Task__priority"], "high")
        self.assertEqual(task_dict["_Task__is_complete"], False)

    def test_from_dict(self):
        """Verifies that Task.from_dict() correctly rebuilds a Task
        with the same name, priority, estimated time, and status.
        """
        original_dict = self.NewTask.to_dict()
        rebuilt = Task.from_dict(original_dict)
        self.assertEqual(rebuilt.name, self.NewTask.name)
        self.assertEqual(rebuilt.get_priority(), self.NewTask.get_priority())
        self.assertEqual(rebuilt.estimated_time, self.NewTask.estimated_time)
        self.assertEqual(rebuilt.get_complete(), self.NewTask.get_complete())

    def test_str_output(self):
        """Verifies that str() on a Task includes its name and the
        'Pending' status.
        """
        self.assertIn(self.NewTask.name, str(self.NewTask))
        self.assertIn("Pending", str(self.NewTask))
        
class TestUrgentTask(unittest.TestCase):
    
    def setUp(self):
        """Creates a fresh UrgentTask instance before each test."""
        super().setUp()
        self.urgent_task = UrgentTask("Fix server outage", 5, "2024-12-01")

    def test_urgent_priority_is_always_high(self):
        """Verifies that an UrgentTask's priority is always 'high',
        regardless of the fact that no priority is passed in explicitly.
        """
        self.assertEqual(self.urgent_task.get_priority(), "high")

    def test_urgent_str_contains_label(self):
        """Verifies that the string representation of an UrgentTask
        includes the '[URGENT]' label.
        """
        self.assertIn("[URGENT]", str(self.urgent_task))

    def test_urgent_str_contains_deadline(self):
        """Verifies that the string representation of an UrgentTask
        includes its deadline.
        """
        self.assertIn(self.urgent_task.deadline, str(self.urgent_task))

    def test_urgent_to_dict_includes_type(self):
        """Verifies that to_dict() on an UrgentTask includes a 'type'
        field equal to 'UrgentTask' and includes the 'deadline' field.
        """
        task_dict = self.urgent_task.to_dict()
        self.assertEqual(task_dict["type"], "UrgentTask")
        self.assertIn("deadline", task_dict)


class TestRecurringTask(unittest.TestCase):
    def setUp(self):
        """Creates a fresh RecurringTask instance before each test."""
        super().setUp()
        self.recurring_task = RecurringTask("Team standup", "medium", 15, "daily")

    def test_recurring_str_contains_label(self):
        """Verifies that the string representation of a RecurringTask
        includes the '[RECURRING' label.
        """
        self.assertIn("[RECURRING", str(self.recurring_task))

    def test_recurring_to_dict_includes_type(self):
        """Verifies that to_dict() on a RecurringTask includes a 'type'
        field equal to 'RecurringTask' and includes the 'frequency' field.
        """
        task_dict = self.recurring_task.to_dict()
        self.assertEqual(task_dict["type"], "RecurringTask")
        self.assertIn("frequency", task_dict)

    def test_reset(self):
        """Verifies that calling reset() after marking a RecurringTask
        complete sets its completion status back to False.
        """
        self.recurring_task.mark_complete()
        self.recurring_task.reset()
        self.assertFalse(self.recurring_task.get_complete())

if __name__ == "__main__":
    unittest.main()