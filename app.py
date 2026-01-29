# app.py
# Modern Dark-Themed To-Do List App

import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager

class TodoApp:
    def __init__(self):
        self.manager = TaskManager()

        self.root = tk.Tk()
        self.root.title("Modern To-Do List")
        self.root.geometry("420x550")
        self.root.config(bg="#1E1E1E")
        self.root.resizable(False, False)

        self.task_input = tk.StringVar()

        self.create_ui()
        self.root.mainloop()

    def create_ui(self):
        tk.Label(
            self.root,
            text="📝 To-Do List",
            font=("Segoe UI", 22, "bold"),
            fg="#00FF9C",
            bg="#1E1E1E"
        ).pack(pady=15)

        entry = tk.Entry(
            self.root,
            textvariable=self.task_input,
            font=("Segoe UI", 14),
            bg="#2D2D2D",
            fg="white",
            insertbackground="white",
            bd=0,
            width=28
        )
        entry.pack(pady=10, ipady=8)

        tk.Button(
            self.root,
            text="Add Task",
            font=("Segoe UI", 12, "bold"),
            bg="#00FF9C",
            fg="#1E1E1E",
            bd=0,
            padx=20,
            pady=8,
            command=self.add_task
        ).pack(pady=10)

        self.listbox = tk.Listbox(
            self.root,
            font=("Segoe UI", 12),
            bg="#2D2D2D",
            fg="white",
            selectbackground="#00FF9C",
            bd=0,
            height=12
        )
        self.listbox.pack(padx=20, pady=15, fill=tk.BOTH)

        btn_frame = tk.Frame(self.root, bg="#1E1E1E")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="✔ Complete", command=self.complete_task,
                  bg="#3CB371", fg="white", bd=0, padx=10).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="🗑 Delete", command=self.delete_task,
                  bg="#FF5555", fg="white", bd=0, padx=10).grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_input.get()
        if not task:
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return
        self.manager.add_task(task)
        self.task_input.set("")
        self.refresh()

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.manager.delete_task(index)
            self.refresh()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.manager.toggle_task(index)
            self.refresh()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first")

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for task in self.manager.get_tasks():
            prefix = "✔ " if task["completed"] else "• "
            self.listbox.insert(tk.END, prefix + task["title"])

if __name__ == "__main__":
    TodoApp()
