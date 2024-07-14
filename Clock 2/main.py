import tkinter as tk
import math
import time

class ModernAnalogClock(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(bg='white')
        self.width = 400
        self.height = 400
        self.create_clock_face()
        self.hands = {}
        self.create_hands()
        self.update_clock()

    def create_clock_face(self):
        # Create clock circle
        self.create_oval(10, 10, 390, 390, outline='#333333', width=2)
        
        # Create hour markers and numbers
        for i in range(12):
            angle = i * math.pi/6 - math.pi/2
            x1 = 200 + 170 * math.cos(angle)
            y1 = 200 + 170 * math.sin(angle)
            x2 = 200 + 180 * math.cos(angle)
            y2 = 200 + 180 * math.sin(angle)
            self.create_line(x1, y1, x2, y2, fill='#333333', width=2)
            
            # Add numbers
            x = 200 + 150 * math.cos(angle)
            y = 200 + 150 * math.sin(angle)
            if i == 0:
                num = 12
            else:
                num = i
            self.create_text(x, y, text=str(num), font=('Arial', 14, 'bold'), fill='#333333')

    def create_hands(self):
        self.hands['second'] = self.create_line(200, 200, 200, 100, width=1, fill='red')
        self.hands['minute'] = self.create_line(200, 200, 200, 80, width=3, fill='#333333')
        self.hands['hour'] = self.create_line(200, 200, 200, 120, width=5, fill='#333333')

    def update_clock(self):
        current_time = time.localtime()
        angles = {
            'second': 6 * current_time.tm_sec,
            'minute': 6 * current_time.tm_min,
            'hour': 30 * (current_time.tm_hour % 12) + current_time.tm_min / 2
        }
        
        for hand, angle in angles.items():
            x = 200 + 180 * math.sin(math.radians(angle))
            y = 200 - 180 * math.cos(math.radians(angle))
            self.coords(self.hands[hand], 200, 200, x, y)
        
        self.after(1000, self.update_clock)

root = tk.Tk()
root.title("Modern Analog Clock")
clock = ModernAnalogClock(root, width=400, height=400)
clock.pack()
root.mainloop()
