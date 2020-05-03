#crossover.py
from random import randint as random_randint, \
     sample as random_sample
def multi_point_crossover(self, point):
    assert (self.ratio & 1) == 0, \
           ('Invalid ratio: %d' % self.ratio)
    children = []
    chromosome_length = len(self.chromosome[0])
    for i in range(0, len(self.chromosome), 2):
        parent = self.chromosome[i], \
                 self.chromosome[i + 1]
        for j in range(self.ratio * 2 - 2):
            a = sorted(random_sample(range(\
                chromosome_length), point))
            a.insert(0, 0)
            a.append(chromosome_length)
            child = []
            for k in range(point + 1):
                child.extend(parent[k & 1][\
                    a[k]:a[k + 1]])
            children.append(child)
    self.chromosome.extend(children)
def one_point_crossover(self):
    return multi_point_crossover(self, 2)
def two_point_crossover(self):
    return multi_point_crossover(self, 3)
def uniform_crossover(self):
    assert (self.ratio & 1) == 0, \
           ('Invalid ratio: %d' % self.ratio)
    children = []
    chromosome_length = len(self.chromosome[0])
    for i in range(0, len(self.chromosome), 2):
        parent = self.chromosome[i], \
                 self.chromosome[i + 1]
        for j in range(self.ratio * 2 - 2):
            child = []
            for k in range(chromosome_length):
                child.append(parent[random_randint(0, 1)][k])
            children.append(child)
    self.chromosome.extend(children)
if __name__ == '__main__':
    import population
    class Test(population.Population):
        fitness = lambda self:self.chromosome
    funclist = [one_point_crossover,
                two_point_crossover,
                uniform_crossover]
    for i in funclist:
        print(i.__name__)
        Test.cross = i
        a = Test([list(range(0, 1000)), list(\
            range(1000, 2000))], 1000, {})
        a.cross()
        print(a.chromosome)
