"""
Task Management Module

Maintains a simple todo list system with task addition/removal functionality.
Integrates with the main interface for productivity tracking.
"""

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Add new task with default incomplete status"""
        self.tasks.append({
            'description': description,
            'completed': False
        })
        return f"Added: {description}"

    def remove_task(self, index):
        """Remove task by index"""
        try:
            removed = self.tasks.pop(index-1)
            return f"Removed: {removed['description']}"
        except IndexError:
            return "Invalid task number"

    def complete_task(self, index):
        try:
            self.tasks[index-1]['completed'] = True
            return f"Marked complete: {self.tasks[index-1]['description']}"
        except IndexError:
            return "Invalid task number"
        except TypeError:
            return "Please enter a valid number"

    def show_tasks(self):
        """Return the formatted task list"""
        if not self.tasks:
            return "No tasks in list"

        output = ["\nTodo List:"]
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else " "
            output.append(f"{i}. [{status}] {task['description']}")
        return '\n'.join(output)

