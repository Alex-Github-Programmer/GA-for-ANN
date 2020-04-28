#network.py
from math import tanh as math_tanh
class Network:
    def __init__(self, h, n, w):
        self.h = h
        self.n = n
        self.w = w
    def simulate(self, arg):
        h = self.h
        n = self.n
        w = self.w
        b = arg.copy()
        for i in range(h - 1):
            a = b.copy()
            for j in range(n[i + 1]):
                b[j] = sum((w[i][j][k] * a[k] \
                           for k in range(n[i])), \
                           start = w[i][j][n[i]])
                b[j] = math_tanh(b[j])
        return b
if __name__ == '__main__':
    a = Network(3, [3, 2, 3], [[[1, 0, 0, 1], [0, 1, 1, 2]], \
                               [[1, -1, 0], [1, 1, 3], [1, 2, -2]]])
    print(a.simulate([1, 2, 3]))
