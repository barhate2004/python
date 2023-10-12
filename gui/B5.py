5. Write a Python GUI program to create Menu widget using tkinter module.

from tkinter import *
top=Tk()
top.geometry("200x300")

def hello():
	print("hello!")
menubar=Menu(top)
menubar.add_command(label="hello!",command=hello)

top.config(menu=menubar)
top.mainloop()
