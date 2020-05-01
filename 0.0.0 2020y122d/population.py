#population.py
class Population:
    def __init__(self, chromosome, number, ratio = 2):
        self.chromosome = chromosome
        self.ratio = ratio
        self.number = number
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
