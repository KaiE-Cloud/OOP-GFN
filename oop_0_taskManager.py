from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority
        self.due_date = due_date

    def mark_complete(self):
        self.completed = True

    def is_overdue(self):
        if datetime.today().strftime("%Y-%m-%d") >= self.due_date: return "Yes"
        else: return "No"

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} - {self.description} - Priority: {self.priority} - Due: {self.is_overdue()} - [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, due_date):
        task = Task(title, description, priority, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()


# Example usage
manager = TaskManager()
manager.add_task("Buy groceries", "Milk, eggs, bread", "Medium", "2025-08-20")
manager.add_task("Study", "Read Python OOP chapter", "High", "2025-08-31")
manager.add_task("Exercise", "Yoga with wifu", "Medium", "2025-08-19")
manager.add_task("Mail", "Presents for party", "High", "2025-08-18")
manager.list_tasks()
manager.complete_task(0)
manager.list_tasks()
