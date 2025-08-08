import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        characters = ""
        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#2C3E50")

# Title Label
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

# Length Entry
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#2C3E50", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, bg="#2C3E50", fg="white", selectcolor="#34495E").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, bg="#2C3E50", fg="white", selectcolor="#34495E").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg="#2C3E50", fg="white", selectcolor="#34495E").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, bg="#2C3E50", fg="white", selectcolor="#34495E").pack(anchor="w", padx=40)

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#16A085", fg="white", command=generate_password).pack(pady=10)

# Result
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 14), justify="center", state="readonly").pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#E67E22", fg="white", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
