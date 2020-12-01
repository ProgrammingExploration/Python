from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk

root = Tk()
root.title("Exploration 10")
root.geometry('400x400')

options = [
    0,
    1,
    2,
    3,
    4
]

drop_value = IntVar()
drop_value.set(options[0])

# Enter Widgets Here
drop = OptionMenu(root, drop_value, *options)
drop.pack()

Label(root, text=str(drop_value.get()), textvariable=drop_value).pack()

def show():
    res = messagebox.askyesno("Popup", "Hello World")

Button(root, text="Show", command=show).pack()

root.filename = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                           filetype=[("PNG File", "*.png"), ("All Files", "*.*")])
img = ImageTk.PhotoImage(Image.open(root.filename))

Label(image=img).pack()

def create():
    new = Toplevel()
    new.title('Hi')
    new.geometry('400x400')
    Button(new, text="Destroy", command=new.destroy).pack()

Button(root, text="Create new Window", command=create).pack()

root.mainloop()
