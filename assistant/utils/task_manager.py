tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added successfully."

def list_tasks():
    if not tasks:
        return "No tasks available."
    return "\n".join([f"{idx + 1}. {task}" for idx, task in enumerate(tasks)])

def clear_tasks():
    tasks.clear()
    return "All tasks cleared."
