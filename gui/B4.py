4. Write a Python GUI program to create three radio buttons widget using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

r1=Radiobutton(top,text="FY")
r1.place(x=100,y=110)

r2=Radiobutton(top,text="TY")
r2.place(x=100,y=80)

r3=Radiobutton(top,text="FY")
r3.place(x=100,y=50)
top.mainloop()
