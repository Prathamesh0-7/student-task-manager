import unittest
from app import app, tasks

class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        tasks.clear()
        self.client = app.test_client()

    def test_home(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_add_task(self):
        self.client.post("/add", data={"title": "Study DevOps"})
        self.assertEqual(tasks[0]["title"], "Study DevOps")

    def test_empty_task(self):
        self.client.post("/add", data={"title": "  "})
        self.assertEqual(len(tasks), 0)

    def test_delete_task(self):
        self.client.post("/add", data={"title": "Test"})
        task_id = tasks[0]["id"]
        self.client.post(f"/delete/{task_id}")
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()
