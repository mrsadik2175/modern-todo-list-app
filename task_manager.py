# task_manager.py

from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if title.strip():
            task = {
                "title": title,
                "completed": False,
                "created_at": datetime.now().strftime("%d %b %Y | %I:%M %p")
            }
            self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def toggle_task(self, index):
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]

    def get_tasks(self):
        return self.tasks
