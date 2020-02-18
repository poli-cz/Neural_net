import numpy as np
import os, sys
#import GUI_master


#print(GUI_master.stop)
class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)

        self.synaptic_weights = 2*np.random.random((50,1))-1

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self, x):
        return x*(1-x)

    def train(self, training_inputs, training_outputs, training_iterations):

       for iteration in range(training_iterations):

            output = self.think(training_inputs)

            print("Output je:")
            print(output)
            print("očekávaná hodnota je:")
            print(training_outputs)

            error = training_outputs-output

            print("error je:")
            print(error)

            adjustments = np.dot(training_inputs.T, error*self.sigmoid_derivative(output))

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


    cwd = os.getcwd()
    str=(cwd+'\\ropa.txt')
    f = open(str, "r")

    data = list()
    for i in range(8308):
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
    print(neural_network.synaptic_weights)
    print("Output data = ")
    print(neural_network.think(testovaci_data))
