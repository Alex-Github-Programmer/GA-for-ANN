#__main__.py
import network
import population
import selection
import crossover
import mutation
import math
import random
class Population(population.Population):
    select = selection.stochastic_tournament
    cross = crossover.uniform_crossover
    mutate = mutation.simple_mutation
    def fitness(self):
        f = []
        for i in self.chromosome:
            a = 0
            for j in i:
                a = (a << 1) | j
            a /= (1 << 16)
            f.append(a * math.sin(10 * math.pi * a) + 10)
        return f
ch = []
for i in range(100):
    ch.append([bool(random.randint(0, 1)) for i in range(19)])
p = Population(ch, 100, {}.fromkeys(range(19), (0.01,)))
print(max(p.fitness()))
for i in range(1000):
    p.evolute()
    print(max(p.fitness()))
