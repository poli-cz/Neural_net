import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
import os, sys
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from pandas import DataFrame
from matplotlib.backend_bases import key_press_handler
from tkinter import *
import threading
import time

################GUI Functions #################################


class gui(threading.Thread):




    def iter():
        number = simpledialog.askstring(title="Number of Iterations",
        prompt="Enter number of Iterations:")
        global stop
        stop = int(number)

    def iteration():
        for i in range(100000):
            print(i)

    def NET_launcher():
        cwd = os.getcwd()
        str=('python '+cwd+'\\master.py')
        threading.Thread(os.system(str)).start()


    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Neural net gui")

        top_frame = tk.Frame(self.root, width=950, height=400).pack()
        bottom_frame = tk.Frame(self.root).pack(side = "bottom")

        btn1 = tk.Button(top_frame, text = "Run calculations", fg = "green", height=3, width=24, command=gui.NET_launcher).place(x=5, y=5)
        btn2 = tk.Button(top_frame, text = "Exit", fg = "red", height=3, width=24, command=exit).place(x=5, y=65)
        btn3 = tk.Button(top_frame, text = "Define number of iterations", fg = "green", height=3, width=24, command=gui.iter ).place(x=5, y=125)
        l2=Label(self.root,text="Synaptic weigts are exported at every stop to \log.txt").place(x=0, y=380)

        self.root.mainloop()



app=gui()


class Runner(threading.Thread):

    def NET_launcher():
        cwd = os.getcwd()
        str=('python '+cwd+'\\master.py')
        threading.Thread(os.system(str)).start()
