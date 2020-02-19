

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
import os, sys
from tkinter import *
import threading

#####constants######
stop=0
learning_coef=1


####################

########## Two way communication ###################




###############################################################


################GUI Functions #################################
class Gui(threading.Thread):

    def iter():
        number = simpledialog.askstring(title="Number of Iterations",
        prompt="Enter number of Iterations:")
        global stop
        stop = int(number)

    def Thread_maker():
            t = threading.Thread(target=Gui.NET_launcher)
            t.start()

    def Thread_killer():
        learning_coef=10
        print(learning_coef)

    def NET_launcher():
        if stop==0:
            print("First define number of iterations")

        cwd = os.getcwd()
        stoped=str(stop)
        print(learning_coef)
        learning_coeficient=str(learning_coef)
        adress_args=('python '+cwd+'\\master.py '+stoped+' '+learning_coeficient)
        print(adress_args)
        os.system(adress_args)

    def __init__(self):


        self.root = tk.Tk()
        self.root.title("Neural net GUI")

        chkValue = tk.BooleanVar()
        chkValue.set(True)

        top_frame = tk.Frame(self.root, width=950, height=400).pack()
        bottom_frame = tk.Frame(self.root).pack(side = "bottom")

        btn1 = tk.Button(top_frame, text = "Run calculations", fg = "green", height=3, width=24, command=Gui.Thread_maker).place(x=5, y=5)
        btn2 = tk.Button(top_frame, text = "Exit", fg = "red", height=3, width=24, command=Gui.Thread_killer).place(x=5, y=65)
        btn3 = tk.Button(top_frame, text = "Define number of iterations", fg = "green", height=3, width=24, command=Gui.iter ).place(x=5, y=125)
        l2=Label(self.root,text="Synaptic weigts are exported at every stop to \log.txt").place(x=0, y=380)
        chkExample = tk.Checkbutton(top_frame, text='10x Learning Coeficient', command=Gui.Thread_killer).place(x=0, y=185)



        self.root.mainloop()

app=Gui()
