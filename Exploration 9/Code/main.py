from tkinter import *

root = Tk()
root.title("Tkinter Advanced")

input = StringVar()
input.set('')

t = StringVar()

Entry(root, textvariable=input).pack()

def get_input():
    print(input.get())
    input.set('')
    t.set('Input has been taken')

Button(root, text="Get", command=get_input).pack()

Label(root, text="", textvariable=t).pack()

x = IntVar()
y = IntVar()

Scale(root, from_=0, to=100, variable=x, orient=HORIZONTAL).pack()
Scale(root, from_=0, to=100, variable=y, orient=HORIZONTAL).pack()

def c():
    root.geometry(f'{x.get()}x{y.get()}')

Button(root, text="Print", command=c).pack()

MODES = [
    "Taco Bell",
    "McDonalds",
    "Burger King",
    "Subway",
    "Chipotle"
]

r = StringVar()
r.set(MODES[0])

text = StringVar()
text.set('')

def select():
    text.set(f'You chose {r.get()}')

for mode in MODES:
    Radiobutton(root, text=mode, variable=r, value=mode).pack()

Button(root, text="Choose", command=select).pack()
Label(root, textvariable=text).pack()

var = IntVar()

Checkbutton(root, text="Check 1", variable=var).pack()

def submit():
    if var.get() == 0:
        print("False")
    else:
        print("True")

Button(root, text="Submit", command=submit).pack()

Label(root, text="New Window").pack()

def new():
    top = Toplevel() # Tk()
    top.title('Second Window')
    top.geometry('400x400')
    Button(top, text="Close", command=top.destroy).pack()

Button(root, text="Create Window", command=new).pack()

root.mainloop()
