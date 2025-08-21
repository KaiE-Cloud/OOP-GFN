class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} - {self.description} [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()


# Example usage
manager = TaskManager()
manager.add_task("Buy groceries", "Milk, eggs, bread")
manager.add_task("Study", "Read Python OOP chapter")
manager.list_tasks()
manager.complete_task(0)
manager.list_tasks()
