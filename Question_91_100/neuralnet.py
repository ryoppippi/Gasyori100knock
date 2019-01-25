import numpy as np

np.random.seed(0)

trainx = np.array(((0,0), (0,1), (1,0), (1,1)), dtype=np.float32)
trainy = np.array((0, 1, 1, 0), dtype=np.float32)

class NN:
    def __init__(self, ind=2, w=10, outd=1, lr=0.01):
        self.w1 = np.random.randn(2, w)
        self.w2 = np.random.randn(w, 1)
        self.b1 = np.random.randn(2, w)
        self.b2 = np.random.randn(2, 1)
        self.lr = lr
        
    def forward(self, x):
        self.w = np.dot(x, self.w1)# + self.b1
        self.wout = np.dot(self.w, self.w2)# + self.b2
        self.out = self.sigmoid(self.wout)
        return self.out

    def sigmoid(self, x):
        return 1. / (1 + np.exp(-x))

    def backward(self, x, y):
        y = y[..., None]
        out_d = (self.out - y) * self.out * (1. - self.out)

        self.w2_e = np.dot(out_d, self.w2.T)
        self.w2_d = self.w2_e * self.w2[..., 0]
        
        self.w2 -= out_d[..., None] * self.w[..., None] #np.dot(self.wout.T, out_d)
        print(self.w2_d.shape, self.w1.shape)
        print(x.shape)
        print(self.w2.shape, out_d.shape)
        w1_d = np.dot(self.w2, out_d[..., None])
        print(w1_d.shape)
        self.w1 -= w1_d * x
        self.w1 -= x * self.w2_d #np.dot(x.T[..., None], self.w2_d[None, ...])
        #self.b1 += np.dot(x.T, self.w2_d)
        #self.d2 = self.w2 * d
        #self.d1 = self.w1 * self.d2.T

    def train(self, x, y):
        self.forward(x)
        self.backward(x, y)

nn = NN()

for i in range(100):
    nn.train(trainx[i%4], trainy[i%4])
    print(nn.forward(trainx))
