import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        result = f"Your BMI is: {bmi:.2f}"
        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for height and weight.")


window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.configure(bg="#E6F3FF")  


title_label = tk.Label(window, text="BMI Calculator", font=("Arial", 24), bg="#E6F3FF")
title_label.pack(pady=20)

height_label = tk.Label(window, text="Height (m):", font=("Arial", 14), bg="#E6F3FF")
height_label.pack()
height_entry = tk.Entry(window, font=("Arial", 14))
height_entry.pack()

weight_label = tk.Label(window, text="Weight (kg):", font=("Arial", 14), bg="#E6F3FF")
weight_label.pack()
weight_entry = tk.Entry(window, font=("Arial", 14))
weight_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi, font=("Arial", 25), bg="white")
calculate_button.pack(pady=20)


window.mainloop()
