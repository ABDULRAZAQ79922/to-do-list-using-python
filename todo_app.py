import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Task List
        self.tasks = []

        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_task = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.entry_task.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", width=12, command=self.add_task, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.complete_task_button = tk.Button(self.button_frame, text="Complete Task", width=12, command=self.complete_task, font=("Arial", 12), bg="#008CBA", fg="white")
        self.complete_task_button.pack(side=tk.LEFT, padx=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", width=12, command=self.delete_task, font=("Arial", 12), bg="#f44336", fg="white")
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

        self.update_task_listbox()

    def add_task(self):
        task_description = self.entry_task.get()
        if task_description:
            self.tasks.append({"description": task_description, "completed": False})
            self.entry_task.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def complete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks[task_index]["completed"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['description']} - {status}")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
