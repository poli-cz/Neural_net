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
from numba import jit
################GUI Functions #################################

def iter():
    number = simpledialog.askstring(title="Number of Iterations",
    prompt="Enter number of Iterations:")
    global stop
    stop = int(number)

#################################################################

#### Main body #### Neural net #########

def Network():
    class NeuralNetwork():

        def __init__(self):
            np.random.seed(1)
            self.synaptic_weights = 2*np.random.random((50,1))-1
            self.error_history = []

        def sigmoid(self, x, deriv=False):
            if deriv == True:
                return x * (1 - x)
            return 1/(1+np.exp(-x))

        #@jit(nopython=True)
        def backpropagation(self):
            self.error  = self.outputs - self.hidden
            delta = self.error * self.sigmoid(self.hidden, deriv=True)
            self.weights += np.dot(self.inputs.T, delta)


        def train(self, training_inputs, training_outputs, training_iterations):


            for iteration in range(training_iterations):

                output= self.think(training_inputs)

                output= self.think(training_inputs)
                print("Output je:")
                print(output)
                print("očekávaná hodnota je:")
                print(training_outputs)

                self.error = training_outputs-output
                self.error_history.append(np.average(np.abs(self.error)))
                #self.error_history.append(self.error[0])

                print("error je:")
                print(self.error)

                adjustments = np.dot(training_inputs.T, self.error*self.sigmoid(output, deriv=True))

                #print("adjustments are:")
                #print(adjustments)
                #print("synaptic weights are:")
                #print(self.synaptic_weights)

                self.synaptic_weights = self.synaptic_weights + adjustments


                ##########
                #print("output po adjustmentu:")
                #print(self.think(training_inputs))
                ##########

        def think(self, inputs):

            inputs = inputs.astype(float)
            output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

            return output

    if __name__ == "__main__":

        neural_network = NeuralNetwork()

        ################################
        #
        #       KONSTANTY
        #
        ################################

        pocet_uceni = 1
        pocet_vstupu = 50

        #print("Random synaptic weights: ")
        #print(neural_network.synaptic_weights)


    ########### Nacitani vstupu ze souboru #########################
        cwd = os.getcwd()
        str=(cwd+'\\data.txt')
        f = open(str, "r")
    #################################################################
        data = list()
        for i in range(20000): #8308
            line = f.readline()
            data.append(float(line))
            #print(data[i])

        plot_list=[]
        for i in range(stop):
            plot_list.append(i)

        training_inputs = np.empty([3,50])

        for pozice in range((len(data)-pocet_vstupu-250)):
            for i in range(pocet_vstupu):
                training_inputs[0][i] = data[pozice+i]
            for i in range(pocet_vstupu):
                training_inputs[1][i] = data[pozice+i+1]
            for i in range(pocet_vstupu):
                training_inputs[2][i] = data[pozice+i+2]

            #print("testovací sady:")
            #print(training_inputs)
            print("traning ", pozice, "/20000")


    ##############stoping for export weights && ploting chart#############

            if(pozice == stop):
                np.savetxt('log.txt', (neural_network.synaptic_weights), fmt="%1.5e")

                fig=plt.figure(figsize=(7,3))
                plt.plot(plot_list, neural_network.error_history)
                plt.ylabel('Error')

                plot = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
                plot.draw()
                plot.get_tk_widget().place(x=220, y=5)

                window.mainloop()
    ##########################################################################


            training_outputs = np.array([data[pozice+pocet_vstupu+1],data[pozice+pocet_vstupu+2],data[pozice+pocet_vstupu+3]]).T
            neural_network.train(training_inputs, training_outputs, pocet_uceni)

        #print("TEST")
        #print("Synaptic weights after training: ")
    #    print(neural_network.synaptic_weights)


        ###################
        #    TESTOVACÍ DATA
        ###################

        testovaci_data = np.empty(50)
        for i in range(50):
            testovaci_data[i] = data[20000+i]
        print("Expected value for this testing input:")
        print(data[20000+i+1])


        print("New situation:")
        #print(neural_network.synaptic_weights)
        print("Output data = ")
        print(neural_network.think(testovaci_data))
#######################################

##############################GUI interference###################################

window = tk.Tk()
window.title("Neural net GUI")

top_frame = tk.Frame(window, width=950, height=400).pack()
bottom_frame = tk.Frame(window).pack(side = "bottom")

btn1 = tk.Button(top_frame, text = "Run calculations", fg = "green", height=3, width=24, command=Network).place(x=5, y=5)
btn2 = tk.Button(top_frame, text = "Exit", fg = "red", height=3, width=24, command=exit).place(x=5, y=65)
btn3 = tk.Button(top_frame, text = "Define number of iterations", fg = "green", height=3, width=24, command=iter ).place(x=5, y=125)
log=Label(window,text="Synaptic weigts are exported at every stop to \log.txt").place(x=0, y=380)

window.mainloop()
