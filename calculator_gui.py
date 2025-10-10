import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            messagebox.showerror("Math error", "Cannot divide by zero.")
            return
        result.set(float(entry1.get()) / denominator)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple GUI Calculator")

entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

plus = tk.Button(root, text="+", width=5, command=add)
plus.grid(row=1, column=0, padx=5, pady=5)

minus = tk.Button(root, text="-", width=5, command=subtract)
minus.grid(row=1, column=1, padx=5, pady=5)

multiply_btn = tk.Button(root, text="*", width=5, command=multiply)
multiply_btn.grid(row=1, column=2, padx=5, pady=5)

divide_btn = tk.Button(root, text="/", width=5, command=divide)
divide_btn.grid(row=1, column=3, padx=5, pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, width=20, relief="sunken")
result_label.grid(row=2, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
