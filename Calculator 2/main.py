import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Modern Calculator")
        master.configure(bg='black')
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        
        result_display = ttk.Entry(self.master, textvariable=self.result_var, justify="right", font=("Arial", 24))
        result_display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
    
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            if button in ['/', '*', '-', '+', '=']:
                ttk.Button(self.master, text=button, command=cmd, style='Orange.TButton').grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
            else:
                ttk.Button(self.master, text=button, command=cmd).grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        
        ttk.Button(self.master, text="C", command=self.clear, style='Orange.TButton').grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
        ttk.Button(self.master, text="√", command=lambda: self.click('sqrt'), style='Orange.TButton').grid(row=row_val, column=col_val+1, sticky="nsew", padx=2, pady=2)
        
        
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=5)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=5)
        
    
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 20), background='black')
        style.configure('Orange.TButton', background='orange')
        
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif key == 'sqrt':
            try:
                result = math.sqrt(float(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0" or self.result_var.get() == "Error":
                self.result_var.set(key)
            else:
                self.result_var.set(self.result_var.get() + key)
    
    def clear(self):
        self.result_var.set("0")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
