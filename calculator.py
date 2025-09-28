import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        
        if height == 0:
            raise ZeroDivisionError
        
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        
        # Category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        category_label.config(text=f"Category: {category}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Height cannot be zero.")

def clear_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="")
    category_label.config(text="")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x280")

# Weight
label_weight = tk.Label(root, text="Enter weight (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Height
label_height = tk.Label(root, text="Enter height (m):")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calc_button = tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

category_label = tk.Label(root, text="", font=("Arial", 12))
category_label.pack(pady=5)

# Run application
root.mainloop()
