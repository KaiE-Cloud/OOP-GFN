from datetime import date, timedelta




#super
class Task:
    #initialize instance attributes
    def __init__(self, title, description, priority, due_date=None):
        self._title = title
        self._description = description
        self._completed = False
        self._priority = priority
        self._status = "✗"
        if due_date == None: self._due_date = None
        elif isinstance(due_date, date): self._due_date = due_date
        else: raise TypeError("due_date must be a date object or None")

    #private property to get today's date
    @property
    def __today(self):
        return date.today()

    #method to mark task as complete
    def mark_complete(self):
        self._completed = True
        self._status = "✓"

    #method to check if task is overdue or due soon
    def is_overdue(self):
        if self._due_date is None or self._completed == True: return ""
        elif self._due_date - timedelta(days=3) <= self.__today < self._due_date: return f"Due soon! ({(self._due_date - self.__today).days} days left)"
        elif self.__today >= self._due_date: return "Overdue!"
        else: return ""

    #method to provide reminders
    def remind(self):
        if self._due_date is None or self._completed == True: return ""
        elif self._due_date - timedelta(days=3) <= self.__today < self._due_date or self.__today >= self._due_date: return f"Reminder: {self._description} – " + self.is_overdue()

    #define string representation
    def __str__(self):
        return f"Task: {self._title} - Description: {self._description} - Priority: {self._priority} - Due: {self._due_date} [{self._status}] {self.is_overdue()}"


#sub
class WorkTask(Task):
    #initialize instance attributes
    def __init__(self, project, title, description, priority, due_date=None):
        super().__init__(title, description, priority, due_date)
        self.__project = project

    #override remind method
    def remind(self):
        base_reminder = super().remind()
        if base_reminder:
            return base_reminder.replace("Reminder:", "Reminder (Work):")
        return ""

    #define string representation
    def __str__(self):
        base_str = super().__str__()
        return base_str.replace("Task:", f"Project: {self.__project} - Subtask:")


#sub
class PersonalTask(Task):
    #initialize instance attributes
    def __init__(self, title, description, location, priority, due_date=None):
        super().__init__(title, description, priority, due_date)
        self.__location = location

    #override remind method
    def remind(self):
        base_reminder = super().remind()
        if base_reminder:
            return base_reminder.replace("Reminder:", "Reminder (Personal):")
        return ""

    #define string representation
    def __str__(self):
        base_str = super().__str__()
        return base_str.replace("Description:", f"Description: {self._description} - Location: {self.__location}")


#manager for functionality
class TaskManager:
    #initialize instance attributes
    def __init__(self):
        self.tasks = []

    #method to add task
    def add_task(self, task):
        self.tasks.append(task)

    #method to list tasks
    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    #method to call reminders
    def call_reminder(self):
        for i, task in enumerate(self.tasks, 0):
            if task.remind(): print(task.remind())

    #method to complete task
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()




#main entry point
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