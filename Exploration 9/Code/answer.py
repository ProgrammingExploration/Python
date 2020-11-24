from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('300x300')

text = StringVar()
text = ''

e = Entry(root)
e.pack()

def answer():
    input = e.get()
    input = str(input)
    if '+' in input:
        a = int(input.split('+')[0])
        b = int(input.split('+')[1])
        text.set(str(a + b))
    elif '-' in input:
        a = int(input.split('-')[0])
        b = int(input.split('-')[1])
        text.set(str(a - b))
    elif '*' in input:
        a = int(input.split('*')[0])
        b = int(input.split('*')[1])
        text.set(str(a * b))
    elif '/' in input:
        a = int(input.split('/')[0])
        b = int(input.split('/')[1])
        text.set(str(a / b))
    else:
        text.set('Error, not a valid input')
    e.delete(0, END)

def clear():
    e.delete(0, END)

Button(root, text="Calculate", command=answer).pack()

Button(root, text="Clear", command=clear).pack()

answer = Label(root, text="Answer", textvariable=text)
answer.pack()

root.mainloop()
