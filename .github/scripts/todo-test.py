import unittest

from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Review prototype")
        self.pool.add_task(task)

        self.assertEqual(len(self.pool.tasks), 1)
        self.assertIs(self.pool.tasks[0], task)

    def test_get_open_tasks(self):
        self.pool.populate()

        titles = [task.title for task in self.pool.get_open_tasks()]

        self.assertEqual(
            titles,
            [
                "Build prototype",
                "Test navigation",
                "Review feedback",
            ],
        )

    def test_get_done_tasks(self):
        self.pool.populate()

        titles = [task.title for task in self.pool.get_done_tasks()]

        self.assertEqual(
            titles,
            [
                "Research user needs",
                "Create wireframes",
                "Review accessibility",
            ],
        )

    def test_mark_completed(self):
        task = Task("Review prototype")
        self.pool.add_task(task)

        task.mark_completed()

        self.assertTrue(task.completed)
        self.assertEqual(task.status, "Done")
        self.assertIn(task, self.pool.get_done_tasks())
        self.assertNotIn(task, self.pool.get_open_tasks())


if __name__ == "__main__":
    unittest.main(verbosity=2)