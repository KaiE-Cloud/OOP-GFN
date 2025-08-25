from datetime import date, timedelta




class Task:
    def __init__(self, title, description, priority, due_date=None):
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority
        self.due_date = due_date

    def mark_complete(self):
        self.completed = True
    '''
    def is_overdue(self):
        if date.today() >= self.due_date: return "Yes"
        else: return "No"
    '''
    def remind(self):
        if self.mark_complete == True: return "Task is completed"
        elif self.due_date - timedelta(days=3) <= date.today() < self.due_date: return f"Due soon! ({(self.due_date - date.today()).days} days left)"
        elif date.today() >= self.due_date: return "Overdue!"
        else: return ""

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"Task: {self.title} - Description: {self.description} - Priority: {self.priority} - Due: {self.due_date} [{status}] {self.remind()}"


class WorkTask(Task):
    def __init__(self, project, title, description, priority, due_date=None):
        super().__init__(title, description, priority, due_date)
        self.project = project

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"Project: {self.project} - Subtask: {self.title} - Description: {self.description} - Priority: {self.priority} - Due: {self.due_date} [{status}] {self.remind()}"


class PersonalTask(Task):
    def __init__(self, title, description, location, priority, due_date=None):
        super().__init__(title, description, priority, due_date)
        self.location = location

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"Task: {self.title} - Description: {self.description} - Location: {self.location} - Priority: {self.priority} - Due: {self.due_date} [{status}] {self.remind()}"




class TaskManager:
    def __init__(self):
        self.tasks = []
    '''
    def add_task(self, title, description, priority, due_date):
        task = Task(title, description, priority, due_date)
        self.tasks.append(task)

    def add_worktask(self, project, title, description, priority, due_date):
        task = WorkTask(project, title, description, priority, due_date)
        self.tasks.append(task)

    def add_personaltask(self, title, description, location, priority, due_date):
        task = PersonalTask(title, description, location, priority, due_date)
        self.tasks.append(task)
    '''
    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()




# Example usage
manager = TaskManager()
manager.add_task(Task("Buy groceries", "Milk, eggs, bread", "Medium", date(2025, 8, 20)))
manager.add_task(Task("Study", "Read Python OOP chapter", "High", date(2025, 8, 24)))
manager.add_task(Task("Exercise", "Yoga with wifu", "Medium", date(2025, 8, 19)))
manager.add_task(Task("Mail", "Presents for party", "High"))
manager.add_task(WorkTask("OOP", "Inheritance", "Create subclasses of `Task`", "High", date(2025, 8, 31)))
manager.add_task(PersonalTask("Hiking", "2h hike with proper gear and essentials", "Schwarzwald", "Small", date(2025, 9, 30)))
print()
manager.list_tasks()
print()
manager.complete_task(0)
manager.list_tasks()
print()
manager.complete_task(4)
manager.list_tasks()
print()
manager.complete_task(5)
manager.list_tasks()
print()