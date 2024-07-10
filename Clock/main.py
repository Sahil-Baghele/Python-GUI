from tkinter import *
from time import *

def update():
    timeString = strftime("%I:%M:%S")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B,%d,%Y")
    dateLabel.config(text=dateString)

    window.after(1000,update)


window = Tk()

timeLabel = Label(window,font=("Arial",50),fg="green",bg="black")
                
                
timeLabel.pack()

dayLabel = Label(window,font=("Ink Free",25))
                        
dayLabel.pack()

dateLabel = Label(window,font=("Ink Free",30))
                        
dateLabel.pack()

update()

window.mainloop()