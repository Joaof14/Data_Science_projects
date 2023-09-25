from keras.datasets import mnist
import numpy as np
import random

(train_X, train_y), (test_X, text_Y) = mnist.load_data()

class CrossEntropyCost:
    def __init__(self) -> None:
        pass

class Network:
    def __init__(self, sizes, cost = CrossEntropyCost):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.cost = cost
        self.default_weight_initializer() 

    def default_weight_initializer(self):
        self.weights = [np.random.rand(y,1) for y in self.sizes[1:]]
        self.biases = [np.random.rand(y,x)/np.sqrt(x) for x,y in zip(self.sizes[:-1], self.sizes[:1])]

    def feedforward(self,a):
        for w,b in self.weights, self.biases:
            a = ativFunc(np.dot(a,w) + b)
        return a
    
    def train(self, eta, epochs, training_data, test_data, E):
        for epoch in epochs:
            for x,y in train_X, train_y:
                pass


    def backprop(self):
        pass

    



def ativFunc(z):
    return 1/(1-np.exp(-z))
    #função sigmoide

def dativFunc(z):
    ativFunc(z)*(1-ativFunc(z))
    #função sigmoide