from keras.datasets import mnist
import numpy as np
import random

(train_X, train_y), (test_X, text_Y) = mnist.load_data()

class CrossEntropyCost:
    def fn(a, y):
        return np.sum(np.nan_to_num(-y*np.log(a)-(1-y)*np.log(1-a)))

    def delta(a,y):
        return a-y

class Network:
    def __init__(self, sizes, cost = CrossEntropyCost):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.cost = cost
        self.default_weight_initializer() 

    def default_weight_initializer(self):
        self.weights = [np.random.rand(y,1) for y in self.sizes[1:]]
        self.biases = [np.random.rand(y,x)/np.sqrt(x) for x,y in zip(self.sizes[:-1], self.sizes[:1])]
    
    def backprop(self, x,y):
        nbs = [np.zeros(b.shape) for b in self.biases]
        nws = [np.zeros(w.shape) for w in self.weights]

        #computando valores antes e depois de passarem pela função de ativação
        a = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w,a) + b
            zs.append(z)
            a = ativFunc(z)
            activations.append(a)

        #backward
        delta = (self.cost)



    def feedforward(self,z):
        for w,b in self.weights, self.biases:
            a = ativFunc(np.dot(a,w) + b)
        return a





def ativFunc(z):
    return 1/(1-np.exp(-z))
    #função sigmoide

def dativFunc(z):
    ativFunc(z)*(1-ativFunc(z))
    #função sigmoide