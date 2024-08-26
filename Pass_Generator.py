import tkinter as tk
from tkinter import messagebox
import random
import string

def generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        password = generator(length)
        result_label.config(text=f"Generated Password: {password}")
        copy_button.config(state=tk.NORMAL)
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

def copy():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Generated Password: ", ""))
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.geometry('500x500+250+250')
root.title("Password Generator")

tk.Label(root, text="Enter the desired password length:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=check)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy, state=tk.DISABLED)
copy_button.pack(pady=10)

root.mainloop()
