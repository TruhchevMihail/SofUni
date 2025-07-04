from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name: str = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        count = len([t for t in self.tasks if t.completed])
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {count} tasks."

    def view_section(self) -> str:
        result = f"Section {self.name}:\n"
        result += '\n'.join([task.details() for task in self.tasks])
        return result
