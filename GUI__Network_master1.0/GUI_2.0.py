import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog, Text
import os, sys
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
import threading
from functools import partial
import subprocess


class neural_net_controller(threading.Thread):

    def iter():
        number = simpledialog.askstring(title="Number of Iterations",
        prompt="Enter number of Iterations:")
        global stop
        stop = int(number)

        number2=simpledialog.askstring(title="Define learning coeficient",
        prompt="Enter learnig coeficient")
        global learning_coef
        learning_coef=number2

    def Thread_maker():
            t = threading.Thread(target=neural_net_controller.NET_launcher)
            t.start()

    def NET_launcher():
        if stop==0:
            print("First define number of iterations")
            return
        cwd = os.getcwd()
        learning_coeficient=str(learning_coef)
        iter_number=str(stop)
        adress_args=('python '+cwd+'\\master2.py '+iter_number+' '+learning_coeficient)
        os.system(adress_args)


    def chart(self):

        error_history=[]
        error_history=np.load('error_history.npy', mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')

        plot_list=[]
        plot_list=np.load('plot_list.npy', mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')

        fig=plt.figure(figsize=(7,3))
        plt.ylim([-100,100])

        plt.plot(plot_list, error_history)
        plt.ylabel('Percentage Error')
        plt.xlabel('Iteration')
        plot = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        plot.draw()
        plot.get_tk_widget().place(relwidth = 1, relheight = 1, relx = 0, rely = 0)

    def importingBut(frame7): #tlacitko na import

        for widget in frame7.winfo_children(): #pro neopakovani vstupu
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
        filetypes = (("txt", "*.txt"),("all files", "*.*"))) #TODO do prvni zavorky ve filetypes dej jakej typ souboru bude na default
        impstf.append(filename)
        print(filename)
        for impst in impstf:    #ukaze nazev importovanych souboru
            label1 = tk.Label(frame7, text = impst, bg = "white")
            label1.pack()

class Gui():
    root = tk.Tk()
    canvas = tk.Canvas(root, height = 720, width = 1280, bg = "Grey")
    canvas.pack()



    #KONEC PROGRESSBARU
    frame1 = tk.Frame(root, bg = "black") #start
    frame1.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.05)
    frame2 = tk.Frame(root, bg = "black") #stop
    frame2.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.12)
    frame3 = tk.Frame(root, bg = "black") #import
    frame3.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.19)
    frame4 = tk.Frame(root, bg = "black") #export
    frame4.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.26)
    frame5 = tk.Frame(root, bg = "black") #graf
    frame5.place(relwidth = 0.8, relheight = 0.5, relx = 0.15, rely = 0.05)
    #frame6 = tk.Frame(root, bg = "black") #imput box
    #frame6.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.33)
    frame7 = tk.Frame(root, bg = "white") #imported files MUZES ZKUSIT VLOZIT I VIC SOUBORU A OBJEVI SE TI TAM
    frame7.place(relwidth = 0.35, relheight = 0.12, relx = 0.02, rely = 0.575)
    frame8 = tk.Frame(root, bg = "black") #start
    frame8.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.45)

    #usrinput1 = tk.Entry(root)
    #canvas.create_window(200, 140, window=usrinput1)
    #usrinput1.place(relwidth = 0.1, relheight = 0.05, relx = 0.02, rely = 0.33)


    #canvas = tk.Canvas(root, height = 720, width = 1280, bg = "white")
    #canvas.pack()

    start = tk.Button(frame1, text = "Iteration number", fg = "black", bg = "green", padx=100,pady=25,
    command=neural_net_controller.iter) #start
    start.pack()
    stop = tk.Button(frame2, text = "stop", fg = "black", bg = "red", padx=100,pady=25,
    command=exit) #stop
    stop.pack()
    imp = tk.Button(frame3, text = "import", fg = "black", bg = "cyan", padx=100,pady=25,
    command=partial(neural_net_controller.importingBut, frame7))  #import
    imp.pack()
    exp = tk.Button(frame4, text = "GO!", fg = "black", bg = "green", padx=100,pady=25,
    command=neural_net_controller.Thread_maker) #export
    exp.pack()
    char = tk.Button(frame8, text = "Build chart", fg = "black", bg = "green", padx=100,pady=25
    , command=partial(neural_net_controller.chart, frame5)) #print chart
    char.pack()


    #c1 = tk.Checkbutton(root, text='Restore Weights',command=var1, onvalue=1, offvalue=0).place(x=40, y=240)



    root.mainloop()
