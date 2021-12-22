from tkinter import *
import jarvis

print(jarvis)

root =Tk()
root.geometry("655x333")

def hello():
    print("Hello tkinter Buttons")
    exec(open("./jarvis.py").read())

def name():
    print("Name is harry")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print now", command=hello)
b1.pack(side=LEFT, padx=23)

root.mainloop()