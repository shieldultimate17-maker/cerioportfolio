
#Project: Smart Calculator with History (GUI)
#Author: Cerio S. Gbedee Sr.
#Title : Cerios' Calculator


import tkinter as tk
from tkinter import messagebox

# Global dictionary to store history
history = {
    "Addition": [],
    "Subtraction": [],
    "Multiplication": [],
    "Division": []
}

# Function for calculations
def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2  # May raise ZeroDivisionError
        else:
            result = None

        # Store in dictionary history
        if result is not None:
            history[operation].append(f"{num1} {operation} {num2} = {result}")
        return result

    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")
        return None
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")
        return None


# Function triggered by button
def perform_operation(operation):
    num1 = entry1.get()
    num2 = entry2.get()
    result = calculate(num1, num2, operation)
    if result is not None:
        result_label.config(text=f"Result: {result}")


# Function to show history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("400x300")

    text_area = tk.Text(history_window, wrap="word")
    text_area.pack(expand=True, fill="both")

    for key, values in history.items():
        text_area.insert(tk.END, f"\n{key}:\n")
        if values:
            for record in values:
                text_area.insert(tk.END, f"   {record}\n")
        else:
            text_area.insert(tk.END, "   No records yet.\n")


# GUI setup
root = tk.Tk()
root.title("Cerios' Calculator with History")
root.geometry("400x350")

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", command=lambda: perform_operation("Addition")).pack(pady=5)
tk.Button(root, text="Subtract", command=lambda: perform_operation("Subtraction")).pack(pady=5)
tk.Button(root, text="Multiply", command=lambda: perform_operation("Multiplication")).pack(pady=5)
tk.Button(root, text="Divide", command=lambda: perform_operation("Division")).pack(pady=5)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# History button
tk.Button(root, text="Show History", command=show_history).pack(pady=5)

# Run the application
root.mainloop()
