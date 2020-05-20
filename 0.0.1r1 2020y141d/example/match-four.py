import GA_for_ANN as ga
def check(l):
    if l[0] != 0:
        v = l[0]
        for i in l[1:]:
            if i != v:
                return 0
    return 1
def merge(a, b):
    a.reverse()
    b.reverse()
    c = []
    while a and b:
        if a[-1][0] > b[-1][0]:
            c.append(a.pop())
        else:
            c.append(b.pop())
    return c
def win(chess):
    for i in range(7):
        for j in range(2):
            if check(chess[i][j:j + 4]):
                return chess[i][j]
    for i in range(3):
        for j in range(6):
            if check([chess[i + k] for k in range(4)]):
                return chess[i][j]
    for i in range(3):
        for j in range(2):
            if check([chess[i + k][j + k] for k in range(4)]):
                return chess[i][j]
    for i in range(3):
        for j in range(4, 6):
            if check([chess[i + k][j - k] for k in range(4)]):
                return chess[i][j]
    return 0
def match(a, b):
    chess = [[0] for i in range(6)] * 7
    length = [0] * 7
    draw = [6] * 7
    while win(chess) == 0 or length != draw:
        
    return win(chess)
class Population(ga.population.Population_network):
    select = selection.stochastic_tournament
    cross = crossover.uniform_crossover
    mutate = mutation.simple_mutation
    def fitness(self):
        c = [*zip([0] * self.number, self.chromosome)]
        for i in range(16):
            a = []
            b = []
            for j in range(0, num, 2):
                k = j + 1
                if match(c[j][0], c[k][0]) == 0:
                    c[j][0] += 1
                    a.append(c[j])
                    b.append(c[k])
                else:
                    c[k][0] += 1
                    a.append(c[k])
                    b.append(c[j])
            c = merge(a, b)

            
