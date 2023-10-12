2. Write a Python GUI program to create a Checkbutton widget using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

c1=Checkbutton(top,text="FY")
c1.pack()

c2=Checkbutton(top,text="SY")
c2.pack()

c3=Checkbutton(top,text="TY")
c3.pack()
top.mainloop()
