from tkinter import *
from tkinter.ttk import *
from time import strftime


root=Tk()
root.title("Clock")
root.resizable(0,0)
logo=PhotoImage(file="./clock.png")
root.iconphoto(False, logo)

def getTime():
	string=strftime("%H: %M: %S: %p")
	label.config(text=string)
	label.after(1000,getTime)

label=Label(root, font=("Lucida Console",40),background="black",foreground="cyan")
label.pack(anchor='center')

if "__main__"==__name__:
	getTime()
	mainloop()