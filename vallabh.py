import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be a positive number.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Copied", "Password copied to clipboard.")


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)


length_entry = tk.Entry(root)
length_entry.pack(pady=5)


password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)


root.mainloop()


