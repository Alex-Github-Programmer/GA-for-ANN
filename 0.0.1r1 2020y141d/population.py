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
class Population_network(Population):
    def __init__(self, chromosome, height, level, number, mutation_dict, ratio = 2):
        self.height = height
        self.level = level
        super().__init__(chromosome, number, mutation_dict, ratio = 2)
    def evolate(self):
        self.select()
        self.chromosome = [i.planarization for i in self.chromosome]
        self.cross()
        self.mutate()
        self.chromosome = [i.restructuration for i in self.chromosome]
def random_population(height, level, number, mutation_dict, ratio = 2):
    return Population_network([random_network(height, level) for i in range(number)], \
                              height, level, number, mutation_dict, ratio = 2)
