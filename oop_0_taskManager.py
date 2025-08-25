from datetime import date, timedelta




class Task:
    def __init__(self, title, description, priority, due_date=None):
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority
        self.status = "✗"
        if due_date == None: self.due_date = None
        elif isinstance(due_date, date): self.due_date = due_date
        else: raise TypeError("due_date must be a date object or None")

    def mark_complete(self):
        self.completed = True
        self.status = "✓"

    def is_overdue(self):
        if self.due_date is None or self.completed == True: return ""
        elif self.due_date - timedelta(days=3) <= date.today() < self.due_date: return f"Due soon! ({(self.due_date - date.today()).days} days left)"
        elif date.today() >= self.due_date: return "Overdue!"
        else: return ""

    def remind(self):
        if self.due_date is None or self.completed == True: return ""
        elif self.due_date - timedelta(days=3) <= date.today() < self.due_date or date.today() >= self.due_date: return f"Reminder: {self.description}"

    def __str__(self):
        return f"Task: {self.title} - Description: {self.description} - Priority: {self.priority} - Due: {self.due_date} [{self.status}] {self.is_overdue()}"


class WorkTask(Task):
    def __init__(self, project, title, description, priority, due_date=None):
        super().__init__(title, description, priority, due_date)
        self.project = project

    def remind(self):
        base_reminder = super().remind()
        if base_reminder:
            return base_reminder.replace("Reminder:", "Reminder (Work):")
        return ""

    def __str__(self):
        base_str = super().__str__()
        return base_str.replace("Task:", f"Project: {self.project} - Subtask:")


class PersonalTask(Task):
    def __init__(self, title, description, location, priority, due_date=None):
        super().__init__(title, description, priority, due_date)
        self.location = location

    def remind(self):
        base_reminder = super().remind()
        if base_reminder:
            return base_reminder.replace("Reminder:", "Reminder (Personal):")
        return ""

    def __str__(self):
        base_str = super().__str__()
        return base_str.replace("Description:", f"Description: {self.description} - Location: {self.location}")




class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def call_reminder(self):
        for i, task in enumerate(self.tasks, 0):
            if task.remind(): print(task.remind())

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()




# Example usage
manager = TaskManager()
manager.add_task(Task("Buy groceries", "Milk, eggs, bread", "Medium", date(2025, 8, 20)))
manager.add_task(Task("Study", "Read Python OOP chapter", "High", date(2025, 8, 24)))
manager.add_task(Task("Exercise", "Yoga with Anna", "Medium", date(2025, 8, 19)))
manager.add_task(Task("Mail", "Presents for party", "High"))
manager.add_task(WorkTask("OOP", "Inheritance", "Create subclasses of `Task`", "High", date(2025, 8, 31)))
manager.add_task(PersonalTask("Hiking", "2h hike with proper gear and essentials", "Schwarzwald", "Small", date(2025, 8, 26)))
print()
manager.list_tasks()
print()
manager.complete_task(0)
manager.list_tasks()
print()
manager.complete_task(4)
manager.list_tasks()
print()
#manager.complete_task(5)
manager.list_tasks()
print()
manager.call_reminder()
print()