import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
import os, sys

window = tk.Tk()
window.title("Neural net gui")


number = simpledialog.askstring(title="NUmber of Iterations",
prompt="Enter number of Iterations:")
stop = int(number)
print(stop)
# End user input#
plot_list=[]
for i in range (stop):
    plot_list.append(i)




def network():
    class NeuralNetwork():

        def __init__(self):
            np.random.seed(1)
            self.synaptic_weights = 2*np.random.random((50,1))-1
            self.error_history = []

        def sigmoid(self, x, deriv=False):
            if deriv == True:
                return x * (1 - x)
            return 1/(1+np.exp(-x))

        def feeding_fuckin_net(self):
            self.hiden =self.sigmoid(np.dot(sefl.inputs, self.synaptic_weights))

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

                print("adjustments are:")
                print(adjustments)
                print("synaptic weights are:")
                print(self.synaptic_weights)

                self.synaptic_weights = self.synaptic_weights + adjustments


                ##########
                print("output po adjustmentu:")
                print(self.think(training_inputs))
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

        print("Random synaptic weights: ")
        print(neural_network.synaptic_weights)


    ########### Nacitani vstupu ze souboru #########################
        cwd = os.getcwd()
        str=(cwd+'\\ropa.txt')
        f = open(str, "r")
    #################################################################
        data = list()
        for i in range(8308): #8308
            line = f.readline()
            data.append(float(line))
            #print(data[i])


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
            print("traning ", pozice, "/8000")


    ##############stoping for export weights && ploting chart#############
            if(pozice == stop):

                np.savetxt('log.txt', (neural_network.synaptic_weights), fmt="%1.5e")

                plt.figure(figsize=(30,5))
                print("error history")
                print(neural_network.error_history)
                plt.plot(plot_list, neural_network.error_history)
                plt.xlabel('Epoch')
                plt.ylabel('Error')
                plt.show()
    ##########################################################################


            training_outputs = np.array([data[pozice+pocet_vstupu+1],data[pozice+pocet_vstupu+2],data[pozice+pocet_vstupu+3]]).T
            neural_network.train(training_inputs, training_outputs, pocet_uceni)

        print("TEST")
        print("Synaptic weights after training: ")
        print(neural_network.synaptic_weights)


        ###################
        #    TESTOVACÍ DATA
        ###################

        testovaci_data = np.empty(50)
        for i in range(50):
            testovaci_data[i] = data[8200+i]
        print("Expected value for this testing input:")
        print(data[8200+i+1])


        print("New situation:")
        #print(neural_network.synaptic_weights)
        print("Output data = ")
        print(neural_network.think(testovaci_data))





top_frame = tk.Frame(window, width=1000, height=1000).pack()
bottom_frame = tk.Frame(window).pack(side = "bottom")

btn1 = tk.Button(top_frame, text = "Run calculations", fg = "green", height=3, width=24, command=network).place(x=5, y=5)
btn2 = tk.Button(top_frame, text = "Stop calculations", fg = "red", height=3, width=24, command=window.quit).place(x=5, y=65)
btn3 = tk.Button(top_frame, text = "Define number of iterations", fg = "green", height=3, width=24, ).place(x=5, y=125)







window.mainloop()
