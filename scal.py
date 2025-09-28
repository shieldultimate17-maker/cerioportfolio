import tkinter as tk
import math

# Function to update expression
def press(key):
    entry.insert(tk.END, key)

# Clear entry
def clear():
    entry.delete(0, tk.END)

# Evaluate expression
def evaluate():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

# Entry widget
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/", "sqrt"],
    ["4", "5", "6", "*", "pow"],
    ["1", "2", "3", "-", "log"],
    ["0", ".", "=", "+", "clear"],
    ["sin", "cos", "tan", "(", ")"]
]

# Create buttons
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        if char == "=":
            btn = tk.Button(root, text=char, width=8, height=2,
                            command=evaluate, bg="lightgreen")
        elif char == "clear":
            btn = tk.Button(root, text=char, width=8, height=2,
                            command=clear, bg="lightcoral")
        else:
            btn = tk.Button(root, text=char, width=8, height=2,
                            command=lambda ch=char: press(ch))
        btn.grid(row=r, column=c, padx=5, pady=5)

# Run application
root.mainloop()
