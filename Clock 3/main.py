import tkinter as tk
from tkinter import ttk
from time import strftime
from datetime import datetime
import pytz

class ModernDigitalClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Modern Digital Clock")
        self.master.geometry("400x250")
        self.master.configure(bg="#2C3E50")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#00FF00", foreground="#ECF0F1", font=("Helvetica", 48))
        self.style.configure("TButton", background="#3498DB", foreground="#ECF0F1", font=("Helvetica", 12))

        self.time_label = ttk.Label(self.master, text="")
        self.time_label.pack()

        self.date_label = ttk.Label(self.master, text="", style="TLabel")
        self.date_label.configure(font=("Helvetica", 18))
        self.date_label.pack()

        self.timezone_var = tk.StringVar()
        self.timezone_var.set("UTC")
        self.timezone_menu = ttk.Combobox(self.master, textvariable=self.timezone_var, values=pytz.all_timezones, state="readonly")
        self.timezone_menu.pack(pady=10)
        self.timezone_menu.bind("<<ComboboxSelected>>", self.update_time)

        self.format_var = tk.StringVar()
        self.format_var.set("24-hour")
        self.format_button = ttk.Button(self.master, text="Toggle 12/24 hour", command=self.toggle_format)
        self.format_button.pack()

        self.update_time()

    def update_time(self, event=None):
        timezone = pytz.timezone(self.timezone_var.get())
        current_time = datetime.now(timezone)
        
        if self.format_var.get() == "24-hour":
            time_string = current_time.strftime('%H:%M:%S')
        else:
            time_string = current_time.strftime('%I:%M:%S %p')
        
        date_string = current_time.strftime('%A, %B %d, %Y')
        
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        self.master.after(1000, self.update_time)

    def toggle_format(self):
        if self.format_var.get() == "24-hour":
            self.format_var.set("12-hour")
        else:
            self.format_var.set("24-hour")
        self.update_time()

if __name__ == "__main__":
    root = tk.Tk()
    clock = ModernDigitalClock(root)
    root.mainloop()
