from tkinter import *
def sum():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    t3.insert(0,c)
win=Tk()
win.geometry('500x500')

l1=Label(win,text="First Number")
l1.grid(row=0,column=0)
t1=Entry(win)
t1.grid(row=0,column=1)

l2=Label(win,text="Second Number")
l2.grid(row=1,column=0)
t2=Entry(win)
t2.grid(row=1,column=1)

l3=Label(win,text="Result")
l3.grid(row=2,column=0)
t3=Entry(win)
t3.grid(row=2,column=1)

b1=Button(win,text="Click For SUM",command=sum)
b1.grid(row=3,column=1)

win.mainloop()
