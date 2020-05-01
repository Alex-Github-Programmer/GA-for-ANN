from random import random as random_random, \
     randint as random_randint, \
     gauss as random_gauss, \
     uniform as random_uniform, \
     choice as random_choice
def simple_mutation(self, mutation_dict):
    for i in self.chromosome:
        for j in mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = not i[j[0]]
def uniform_mutation(self, mutation_dict):
    for i in self.chromosome:
        for j in mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = random_uniform(j[1][1], j[1][2])
def boundary_mutation(self, mutation_dict):
    for i in self.chromosome:
        for j in mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = random_choice([j[1][1], j[1][2]])
def ununiform_mutation(self, mutation_dict):
    for i in self.chromosome:
        for j in mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] = random_uniform(
                    j[1][1] + i[j[0]],
                    j[1][2] + i[j[0]])
def gauss_mutation(self, mutation_dict, p = 1):
    for i in self.chromosome:
        for j in mutation_dict.items():
            value = random_random()
            if value < j[1][0]:
                i[j[0]] += random_gauss(0, p)
if __name__ == '__main__':
    import population
    class Test(population.Population):
        fitness = lambda self:self.chromosome
    funclist = [simple_mutation,
                uniform_mutation,
                boundary_mutation,
                ununiform_mutation,
                gauss_mutation]
    for i in funclist:
        print(i.__name__)
        Test.mutation = i
        a = Test([[i] for i in range(1000)], 1000, 1)
        a.mutation({0:(0.1, 1, 1000)})
        print(a.chromosome)
