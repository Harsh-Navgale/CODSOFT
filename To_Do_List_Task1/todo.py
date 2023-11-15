import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.load_tasks()
        self.create_widgets()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def show_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks found. Start adding tasks!")
        else:
            task_text = "Your To-Do List:\n"
            for index, task in enumerate(self.tasks, start=1):
                task_text += f"{index}. {task['title']} - {task['due_date']}\n"
            messagebox.showinfo("To-Do List", task_text)

    def add_task(self):
        title = self.title_entry.get()
        due_date = self.date_entry.get()

        if not title or not due_date:
            messagebox.showwarning("To-Do List", "Please enter both title and due date.")
            return

        new_task = {
            'title': title,
            'due_date': due_date,
            'created_at': str(datetime.now())
        }

        self.tasks.append(new_task)
        self.save_tasks()
        messagebox.showinfo("To-Do List", "Task added successfully!")

        self.title_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Task Title:")
        title_label.grid(row=0, column=0, padx=10, pady=5)

        self.title_entry = tk.Entry(self.root, width=30)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        date_label = tk.Label(self.root, text="Due Date (YYYY-MM-DD):")
        date_label.grid(row=1, column=0, padx=10, pady=5)

        self.date_entry = tk.Entry(self.root, width=30)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        show_button = tk.Button(self.root, text="Show Tasks", command=self.show_tasks)
        show_button.grid(row=2, column=0, columnspan=2, pady=10)

        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
