#network.py
from math import tanh as math_tanh
class Network:
    def __init__(self, height, level, weight):
        self.height = height
        self.level = level
        self.weight = weight
    def simulate(self, arg):
        height = self.height
        level = self.level
        weight = self.weight
        b = arg.copy()
        for i in range(height):
            a = b.copy()
            for j in range(level[i + 1]):
                b[j] = sum((weight[i][j][k] * a[k] \
                           for k in range(level[i])), \
                           start = weight[i][j][level[i]])
                b[j] = math_tanh(b[j])
        return b
    def planarization(self):
        plain = []
        for i in self.weight:
            for j in i:
                plain.extend(j)
        return (self.height, self.level, plaisn)
    @staticmethod
    def restructuration(group):
        height, level, plain = group
        self = Network(height, level, [])
        for i in range(height):
            self.weight.append([])
            for j in range(level[i + 1]):
                self.weight[-1].append(plain[:level[i] + 1])
                del plain[:level[i] + 1]
                    
        return self
if __name__ == '__main__':
    a = Network(2, [3, 2, 3], [[[1, 0, 0, 1], [0, 1, 1, 2]], \
                               [[1, -1, 0], [1, 1, 3], [1, 2, -2]]])
    print(a.simulate([1, 2, 3]))
    b = a.planarization()
    print(b)
    c = Network.restructuration(b)
    print(a.weight)
    print(c.weight)
    assert a.weight == c.weight, 'Restructuration error'
