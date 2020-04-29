#population.py
class Population:
    def __init__(self, chromosome, ratio):
        self.chromosome = chromosome
        self.ratio = ratio
    def fitness(self):
        return NotImplemented
    def selection(self):
        return NotImplemented
    def crossover(self):
        return NotImplemented
    def mutation(self):
        return NotImplemented
    def evolution(self):
        selection(self)
        heredity(self)
        variation(self)
