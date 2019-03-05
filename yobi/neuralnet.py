import numpy as np

np.random.seed(4)

class NN:
    def __init__(self, ind=2, w=10, outd=1, lr=1):
        self.w2 = np.random.randn(ind, w)
        self.w3 = np.random.randn(w, outd)
        self.b2 = np.random.randn(w)
        self.b3 = np.random.randn(1)
        self.lr = lr
        
    def forward(self, x):
        self.z1 = x
        #self.z1 = np.hstack((x, [1]))
        # add bias
        self.z2 = sigmoid(np.dot(self.z1, self.w2) + self.b2)
        # add bias
        #self.z2 = np.hstack((self.z2, [1]))
        self.z3 = np.dot(self.z2, self.w3) + self.b3
        self.out = sigmoid(self.z3)
        return self.out

    def backward(self, x, t):
        #w3_d = (self.out * (1 - self.out)) * (self.out - y)
        #xw3_delta = np.dot(self.w3.T * (self.out - xy), (self.out) * (1 - self.out))
        #w3_dW = w3_d * self.z2.T[..., None]
        #w3_dB = w3_d

        w3_d = 2 * (self.out - t) * sigmoid_derivative(self.out)
        print(self.w3.shape)
        print(w3_d.shape)
        print(self.w3.T.shape)
        w3_dW = np.dot(self.w2.T, w3_d)
        w3_dB = w3_d
        
        self.w3 -= self.lr * w3_dW
        self.b3 -= self.lr * w3_dB

        #w2_d = np.dot((self.z2 * (1 - self.z2))[..., None], (self.z3.T * w3_d))
        w2_d = np.dot(self.z3.T, w3_d) * (self.z2) * (1 - self.z2)
        w2_dW = w2_d[..., None] * self.z1
        w2_dB = w2_d

        self.w2 += self.lr * w2_dW
        self.b2 += self.lr * w2_dB
        
    def train(self, x, t):
        self.forward(x)
        self.backward(x, t)


class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


def sigmoid(x):
    return 1. / (1. + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1. - sigmoid(x))

trainx = np.array(((0,0), (0,1), (1,0), (1,1)), dtype=np.float32)
trainy = np.array((0, 1, 1, 0), dtype=np.float32)

nn = NN()

nn2 = NeuralNetwork(trainx, trainy)

for i in range(10000):
    """
    for j in range(4):
        nn.train(trainx[j%4], trainy[j%4])
    #print("epoch: " , i)
    for j in range(4):
        if i == 0 or i == 9999:
            print(nn.forward(trainx[j]), end=' ')
    #print()
    """
    nn2.feedforward()
    nn2.backprop()

    print(nn2.output)
