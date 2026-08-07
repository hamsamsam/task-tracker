import unittest
from task import Task, UrgentTask, RecurringTask

class TestTask(unittest.TestCase):
    
    def setUp(self):
        self.NewTask = Task("Buy groceries", "high", 30)
        return super().setUp()
    
    def test_task_creation(self):
        self.assertEqual(self.NewTask.name, "Buy groceries")
        self.assertEqual(self.NewTask.get_priority, "high")
        self.assertEqual(self.NewTask.estimated_time, 30)
        
    def test_mark_compelte(self):
        self.NewTask.mark_complete()
        self.assertEqual(self.NewTask.get_complete, True)
    
    def test_set_priority_value(self):
        self.NewTask.set_priority("Low")
        self.assertEqual(self.NewTask.get_priority(),'low')
    
    def test_set_priority_invalid(self):
        self.NewTask.set_priority("urgent")
        self.assertEqual(self.NewTask.get_priority(), "low")

    def test_set_priority_valid(self):
        self.NewTask.set_priority("medium")
        self.assertEqual(self.NewTask.get_priority(), "medium")

    def test_to_dict(self):
        task_dict = self.NewTask.to_dict()
        self.assertEqual(task_dict["name"], "Buy groceries")
        self.assertEqual(task_dict["estimated_time"], 30)
        self.assertEqual(task_dict["_Task__priority"], "high")
        self.assertEqual(task_dict["_Task__is_complete"], False)

    def test_from_dict(self):
        original_dict = self.NewTask.to_dict()
        rebuilt = Task.from_dict(original_dict)
        self.assertEqual(rebuilt.name, self.NewTask.name)
        self.assertEqual(rebuilt.get_priority(), self.NewTask.get_priority())
        self.assertEqual(rebuilt.estimated_time, self.NewTask.estimated_time)
        self.assertEqual(rebuilt.get_complete(), self.NewTask.get_complete())

    def test_from_dict_marks_complete(self):
        self.NewTask.mark_complete()
        rebuilt = Task.from_dict(self.NewTask.to_dict())
        self.assertTrue(rebuilt.get_complete())

    def test_mark_complete(self):
        self.assertFalse(self.NewTask.get_complete())
        self.NewTask.mark_complete()
        self.assertTrue(self.NewTask.get_complete())

    def test_str_output(self):
        self.assertIn(self.NewTask.name, str(self.NewTask))
        self.assertIn("Pending", str(self.NewTask))
