from tkinter import *
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock By Reyansh")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)


clock = Label(master,font=("Calibri", 90), bg="light blue", fg="black")
clock.pack()

get_time()

master.mainloop()