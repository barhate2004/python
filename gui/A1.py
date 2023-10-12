Write a Python GUI program to add a button in your application using tkinter module.
from tkinter import *
top=Tk()

top.geometry("200x300")
bt=Button(top,text="button")

bt.place(x=100,y=100)
top.mainloop()
