import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class ColorfulCalendar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Colorful Calendar")
        self.geometry("400x400")
        self.configure(bg="#F0F0F0")

        self.current_date = datetime.now()
        self.create_widgets()

    def create_widgets(self):
        # Month and Year selection
        self.month_var = tk.StringVar(value=self.current_date.strftime("%B"))
        self.year_var = tk.StringVar(value=str(self.current_date.year))

        month_combo = ttk.Combobox(self, textvariable=self.month_var, values=list(calendar.month_name)[1:], width=10)
        month_combo.grid(row=0, column=0, padx=5, pady=5)
        month_combo.bind("<<ComboboxSelected>>", self.update_calendar)

        year_entry = ttk.Entry(self, textvariable=self.year_var, width=6)
        year_entry.grid(row=0, column=1, padx=5, pady=5)
        year_entry.bind("<Return>", self.update_calendar)

        
        self.cal_frame = tk.Frame(self, bg="#FFFFFF")
        self.cal_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.update_calendar()

    def update_calendar(self, event=None):
        month = list(calendar.month_name).index(self.month_var.get())
        year = int(self.year_var.get())

        # Clear previous calendar
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        
        cal = calendar.monthcalendar(year, month)

        
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(weekdays):
            lbl = tk.Label(self.cal_frame, text=day, bg="#4CAF50", fg="white", width=6, height=2)
            lbl.grid(row=0, column=i, padx=1, pady=1)

        # Calendar days
        for week_num, week in enumerate(cal, start=1):
            for weekday, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.cal_frame, text=str(day), width=6, height=2)
                    btn.grid(row=week_num, column=weekday, padx=1, pady=1)
                    
                    
                    if weekday >= 5:  
                        btn.configure(bg="#FFA07A")
                    elif week_num % 2 == 0:  
                        btn.configure(bg="#E0FFFF")
                    else:  
                        btn.configure(bg="#F0FFFF")

if __name__ == "__main__":
    app = ColorfulCalendar()
    app.mainloop()

