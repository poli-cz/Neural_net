import tkinter as tk

name= tk.Tk()

canvas1 = tk.Canvas(name, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (name)
canvas1.create_window(200, 140, window=entry1)
number=0
def fcion1():
    x1 = entry1.get()
    label1 = tk.Label(name, text= int(x1))
    number=x1
    canvas1.create_window(200, 230, window=label1)
    return number

button1 = tk.Button(text='LabelText', command=fcion1)
canvas1.create_window(200, 180, window=button1)
name.mainloop()
i = 0
number = int(fcion1())
for i in range(number):
    print(i)
