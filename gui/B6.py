6. Write a Python GUI program to create entry widget using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

e1=Entry(top)
e1.place(x=100,y=100)

e2=Entry(top)
e2.place(x=100,y=60)
top.mainloop()
