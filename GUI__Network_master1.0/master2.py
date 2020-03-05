import numpy as np
import os, sys

global stop
global learning_coeficient
learning_coeficient=int(sys.argv[2])
stop=int(sys.argv[1])


plot_list=[]

for i in range ((stop+1)*learning_coeficient):
    plot_list.append(i)

class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2*np.random.random((50,1))-1
        self.error_history = []

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self, x):
        return x*(1-x)

    def train(self, training_inputs, training_outputs, training_iterations, learning_velocity):

        for iteration in range(training_iterations*learning_coeficient):

            output = self.think(training_inputs)
            error = training_outputs-output

            chyba=(error/(output/100))
            self.error_history.append(np.abs(np.average(error)))

            print("error je:")
            print(error)

            adjustments = learning_velocity*np.dot(training_inputs.T, error) # původně error*self.sigmoid_derivative(output)

            self.synaptic_weights = self.synaptic_weights + adjustments


            ##########
            print("output po adjustmentu:")
            print(self.think(training_inputs))
            ##########





    def think(self, inputs):

        inputs = inputs.astype(float)
        output = np.dot(inputs, self.synaptic_weights) #původně self.sigmoid(np.dot(inputs, self.synaptic_weights))

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
    learning_velocity = 0.00001

    print("Random synaptic weights: ")
    print(neural_network.synaptic_weights)

    cwd = os.getcwd()
    data_zdroj=(cwd+'\\ropa.txt')
    f = open(data_zdroj, "r")

    data = list()
    for i in range(8308):
        line = f.readline()
        data.append((float(line)/100))
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
        print("training ", pozice, "/8000")

        training_outputs = np.array([data[pozice+pocet_vstupu+1],data[pozice+pocet_vstupu+2],data[pozice+pocet_vstupu+3]]).T

        neural_network.train(training_inputs, training_outputs, pocet_uceni, learning_velocity)


        if(pozice == stop):
            print('DONE')
            np.save('error_history', neural_network.error_history, allow_pickle=True, fix_imports=True)
            np.save('plot_list', plot_list, allow_pickle=True, fix_imports=True)
            exit()
    #print("TEST")

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
