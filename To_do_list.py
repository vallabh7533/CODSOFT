import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)


root = tk.Tk()
root.title("To-Do List")


listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


root.mainloop()