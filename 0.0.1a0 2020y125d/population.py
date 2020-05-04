#population.py
class Population:
    def __init__(self, chromosome, number, mutation_dict, ratio = 2):
        self.chromosome = chromosome
        self.number = number
        self.mutation_dict = mutation_dict
        self.ratio = ratio
    def fitness(self):
        return NotImplemented
    def select(self):
        return NotImplemented
    def cross(self):
        return NotImplemented
    def mutate(self):
        return NotImplemented
    def evolute(self):
        self.select()
        self.cross()
        self.mutate()
