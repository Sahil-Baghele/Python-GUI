import tkinter as tk
from tkinter import ttk

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set(None)

def submit_form():
   
    print("Form submitted!")

root = tk.Tk()
root.title("Registration Form")
root.configure(bg='light yellow')


font_style = ('Arial', 25)


tk.Label(root, text="Name:", font=font_style, bg='light yellow').grid(row=0, column=0, sticky='w', padx=10, pady=10)
name_entry = tk.Entry(root, font=font_style)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:", font=font_style, bg='light yellow').grid(row=1, column=0, sticky='w', padx=10, pady=10)
email_entry = tk.Entry(root, font=font_style)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age:", font=font_style, bg='light yellow').grid(row=2, column=0, sticky='w', padx=10, pady=10)
age_entry = tk.Entry(root, font=font_style)
age_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Gender:", font=font_style, bg='light yellow').grid(row=3, column=0, sticky='w', padx=10, pady=10)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", font=font_style, bg='light yellow').grid(row=3, column=1, sticky='w', padx=10, pady=5)

tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", font=font_style, bg='light yellow').grid(row=4, column=1, sticky='w', padx=10, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields, font=font_style)
clear_button.grid(row=5, column=0, padx=10, pady=20)

submit_button = tk.Button(root, text="Submit", command=submit_form, font=font_style)
submit_button.grid(row=5, column=1, padx=10, pady=20)

root.mainloop()


