import numpy as np

np.random.seed(0)

trainx = np.array(((0,0), (0,1), (1,0), (1,1)), dtype=np.float32)
trainy = np.array((0, 1, 1, 0), dtype=np.float32)

class NN:
    def __init__(self, ind=2, w=100, outd=1, lr=0.01):
        self.w1 = np.random.randn(ind, w)
        self.w2 = np.random.randn(w, outd)
        self.lr = lr
        
    def forward(self, x):
        w = np.dot(x, self.w1)
        wout = np.dot(w, self.w2)
        wout = self.sigmoid(wout)
        return wout

    def sigmoid(self, x):
        return 1. / (1 + np.exp(-x))

    def loss(self, x, y):
        return -np.sum(((x - y) ** 2) / 2.) / y.shape[0]

    def backward(self, d):
        self.d2 = self.w2 * d
        self.d1 = self.w1 * self.d2.T

    def update(self):
        self.w2 -= self.lr * self.d2
        self.w1 -= self.lr * self.d1

    def train(self, x, y):
        wout = self.forward(x)
        loss = self.loss(wout, y)
        self.backward(loss)
        self.update()


nn = NN()

for _ in range(10):
    nn.train(trainx, trainy)
    print(nn.forward(trainx))
