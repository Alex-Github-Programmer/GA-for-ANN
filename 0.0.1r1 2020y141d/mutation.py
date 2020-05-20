from random import random as random_random, \
     randint as random_randint, \
     gauss as random_gauss, \
     uniform as random_uniform, \
     choice as random_choice
def simple_mutation(self):
    for i in self.children:
        for j in self.mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = not i[j[0]]
    self.chromosome.extend(self.children)
    del self.children
def uniform_mutation(self):
    for i in self.children:
        for j in self.mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = random_uniform(j[1][1], j[1][2])
    self.chromosome.extend(self.children)
    del self.children
def boundary_mutation(self):
    for i in self.children:
        for j in self.mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = random_choice([j[1][1], j[1][2]])
    self.chromosome.extend(self.children)
    del self.children
def ununiform_mutation(self):
    for i in self.children:
        for j in self.mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = random_uniform(
                    j[1][1] + i[j[0]],
                    j[1][2] + i[j[0]])
    self.chromosome.extend(self.children)
    del self.children
def gauss_mutation(self, p = 1):
    for i in self.children:
        for j in self.mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] += random_gauss(0, p)
    self.chromosome.extend(self.children)
    del self.children
if __name__ == '__main__':
    import population
    class Test(population.Population):
        fitness = lambda self:self.children
    funclist = [simple_mutation,
                uniform_mutation,
                boundary_mutation,
                ununiform_mutation,
                gauss_mutation]
    for i in funclist:
        print(i.__name__)
        Test.mutate = i
        a = Test([], 1000, {0:(0.1, 1, 1000)})
        a.children = [[i] for i in range(1000)]
        a.mutate()
        print(a.chromosome)
