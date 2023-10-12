2. Write a Python GUI program to create two buttons exit and hello using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

bt1=Button(top,text="exit")
bt1.place(x=100,y=100)

bt2=Button(top,text="hello")
bt2.place(x=50,y=50)
top.mainloop()
