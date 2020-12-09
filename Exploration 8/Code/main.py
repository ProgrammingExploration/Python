from tkinter import *

# Create Instance
root = Tk()
root.title('Hello')

# Widgets
input = Entry(root, width=50, borderwidth=5)
input.pack()

second = Entry(root, width=50, borderwidth=5)
second.pack()

def click():
    a = input.get()
    b = second.get()
    try:
        a = int(a)
        b = int(b)
        l = Label(root, text=str(a + b))
        l.pack()
    except:
        l = Label(root, text="Error, not an integer")
        l.pack()

label = Label(root, text="Hello World")
label.pack()

Button(root, text="Button", command=click, fg="yellow", bg="red").pack()

root.mainloop()
