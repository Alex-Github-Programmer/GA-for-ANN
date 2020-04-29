#selection.py
from random import random as random_random
def roulette_wheel_selection(self):
    size = int(len(self.chromosome) * self.ratio)
    a = dict(enumerate(self.fitness()))
    b = []
    s = sum(a)
    for i in range(size):
        k = random_random() * s
        n = 0
        x = iter(a)
        while n < k:
            m = next(x)
            n += a[m]
        s -= a.pop(m)
        b.append(self.chromosome[m])
    self.chromosome = b
def stochastic_tournament(self):
    size = int(len(self.chromosome) * self.ratio)
    a = dict(enumerate(self.fitness()))
    b = []
    s = sum(a)
    for i in range(size):
        k = random_random() * s
        n = 0
        x = iter(a)
        while n < k:
            p = next(x)
            n += a[p]
        
        k = random_random() * s
        n = 0
        x = iter(a)
        while n < k:
            q = next(x)
            n += a[q]
        b.append(self.chromosome[p if a[p] > a[q] else q])
        s -= a.pop(p if a[p] > a[q] else q)
    self.chromosome = b
if __name__ == '__main__':
    import population
    class Test(population.Population):
        fitness = lambda self:self.chromosome
    funclist = [roulette_wheel_selection,
                stochastic_tournament]
    for i in funclist:
        print(i.__name__)
        Test.selection = i
        a = Test(list(range(1000)), 0.5)
        a.selection()
        print(sorted(a.chromosome))
