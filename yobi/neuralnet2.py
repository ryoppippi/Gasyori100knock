import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, t):
        self.z1      = x
        self.w2   = np.random.rand(self.z1.shape[1],3)
        self.w3   = np.random.rand(3,1)
        self.t          = t
        self.out     = np.zeros(self.t.shape)

    def feedforward(self):
        self.z2 = sigmoid(np.dot(self.z1, self.w2))
        self.out = sigmoid(np.dot(self.z2, self.w3))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to w3 and w2
        d_w3 = np.dot(self.z2.T, (2*(self.t - self.out) * sigmoid_derivative(self.out)))
        d_w2 = np.dot(self.z1.T, (np.dot(2*(self.t - self.out) * sigmoid_derivative(self.out), self.w3.T) * sigmoid_derivative(self.z2)))

        # update the weights with the derivative (slope) of the loss function
        self.w2 += d_w2
        self.w3 += d_w3


if __name__ == "__main__":
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],[1],[1],[0]])
    nn = NeuralNetwork(X,y)
    print(X.shape, y.shape)
    for i in range(15000):
        nn.feedforward()
        nn.backprop()

    print(nn.out)
