#procedural 




tasks = []

def add_task(title, description):
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)

def list_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} - {task['description']} [{status}]")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True


# Example usage
add_task("Buy groceries", "Milk, eggs, bread")
add_task("Study", "Read Python OOP chapter")
list_tasks()
complete_task(0)
list_tasks()
