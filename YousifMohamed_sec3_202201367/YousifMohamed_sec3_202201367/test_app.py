import unittest
from app import add_task, get_tasks, tasks

class TestToDoApp(unittest.TestCase):
    def setUp(self):

        tasks.clear()

    def test_add_task(self):
        add_task("swe")
        self.assertEqual(get_tasks(), ["swe"])

    def test_get_tasks(self):
        self.assertEqual(get_tasks(), [])

        add_task("stat")
        self.assertEqual(get_tasks(), ["stat"])

if __name__ == "__main__":
    unittest.main()
