class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False  # starts incomplete

task = Task("Finish project", "Due next week")
print(task.completed)
task.completed = "yes"  # direct assignment from outside
print(task.completed)