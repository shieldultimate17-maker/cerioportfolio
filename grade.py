
#Project: Student Report Card (GUI)
#Author: Cerio S. Gbedee



import tkinter as tk
from tkinter import messagebox

# Dictionary to store student records
students = {}

# Function to calculate report card
def generate_report(name, marks_dict):
    try:
        total = sum(marks_dict.values())
        average = total / len(marks_dict)  # ZeroDivisionError possible
       
        # Grading system
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"
        # Return result as dictionary
        return {
            "Name": name,
            "Marks": marks_dict,
            "Total": total,
            "Average": round(average, 2),
            "Grade": grade
        }
    except ZeroDivisionError:
        messagebox.showerror("Error", "No subjects entered. Please add at least one subject.")
        return None


# Function triggered on button click
def create_report():
    name = entry_name.get()
    subject = entry_subject.get()
    mark = entry_mark.get()

    if not name or not subject or not mark:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    try:
        mark = float(mark)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for marks.")
        return

    # Add student record
    if name not in students:
        students[name] = {}
    students[name][subject] = mark

    messagebox.showinfo("Success", f"Added {subject} with marks {mark} for {name}.")

    entry_subject.delete(0, tk.END)
    entry_mark.delete(0, tk.END)


# Function to display report card
def show_report():
    name = entry_name.get()
    if name not in students:
        messagebox.showerror("Not Found", f"No record found for {name}.")
        return

    report = generate_report(name, students[name])
    if report:
        report_window = tk.Toplevel(root)
        report_window.title(f"{name}'s Report Card")
        report_window.geometry("400x400")

        text_area = tk.Text(report_window, wrap="word")
        text_area.pack(expand=True, fill="both")

        text_area.insert(tk.END, f"Report Card for {report['Name']}\n")
        text_area.insert(tk.END, "-"*40 + "\n")
        for subject, mark in report["Marks"].items():
            text_area.insert(tk.END, f"{subject}: {mark}\n")
        text_area.insert(tk.END, "-"*40 + "\n")
        text_area.insert(tk.END, f"Total: {report['Total']}\n")
        text_area.insert(tk.END, f"Average: {report['Average']}\n")
        text_area.insert(tk.END, f"Grade: {report['Grade']}\n")


# GUI Setup
root = tk.Tk()
root.title("Student Report Card System")
root.geometry("400x400")

tk.Label(root, text="Student Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Subject:").pack()
entry_subject = tk.Entry(root)
entry_subject.pack()

tk.Label(root, text="Marks:").pack()
entry_mark = tk.Entry(root)
entry_mark.pack()

tk.Button(root, text="Add Subject & Marks", command=create_report).pack(pady=5)
tk.Button(root, text="Generate Report Card", command=show_report).pack(pady=5)

root.mainloop()
