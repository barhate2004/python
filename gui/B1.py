1. Write a Python GUI program to create a Listbox with three options using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

lb=Listbox(top,height=3)
lb.insert(1,"FY")
lb.insert(2,"SY")
lb.insert(3,"TY")

lb.place(x=100,y=100)
top.mainloop()
