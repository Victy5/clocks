from tkinter import *
import time

a = Tk()
a.title("Digital Clock")

def time_update():
    current_time = time.strftime("%H:%M:%S:")
    #possible %a,%b, %c, Date in full %D, month %m, date %d, month in words %h, number of days in a year %j
    clock.config(text=current_time)
    clock.after(1, time_update)

clock = Label(a, font=("caribri", 70, "bold"), width=7, bg="light blue", fg= "black")
clock.pack(fill="both", expand=True)
time_update()

a.mainloop()