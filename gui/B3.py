. Write a Python GUI program to create three single line text-box to accept a value from the
user using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

e1=Entry(top)
e1.place(x=100,y=100)

e2=Entry(top)
e2.place(x=80,y=80)

e3=Entry(top)
e3.place(x=60,y=60)
top.mainloop()


