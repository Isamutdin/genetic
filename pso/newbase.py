from copy import deepcopy
import random


class Array(list):
    
    def __add__(self, other):
        result = Array()
        term = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
        for n in range(len(self)):
            result.append(self[n]+term[n])
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        result = Array()
        other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
        for n in range(len(self)):
            result.append(self[n]-other[n])
        return result

    def __rsub__(self, other): 
        result = Array()
        other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
        for n in range(len(self)):
            result.append(other[n]-self[n])
        return result

    def __mul__(self, other):
        result = Array()
        other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
        for n in range(len(self)):
            result.append(other[n]*self[n])
        return result

    def __rmul__(self, other):
        return self.__mul__(other)


class Particle(Array):
    def __init__(self, *args):
        super().__init__(*args)
        self.velocity = Array([0 for i in range(len(self))])
        self.fitness = Fitness()
        self.best = Array([pos for pos in self])
        self.fitbest = Fitness(-(10**6))



class Fitness(object):

    weight = 1 

    wvalue = 0 

    def __init__(self, value=None) -> None:
        self.value = value

    def setValue(self, value) -> None:
        self.wvalue = value*self.weight
        self.value = value

    def getValue(self):
        return self.wvalue

    def delValues(self) -> None:
        self.wvalue = 0

    #Сравнение Fitness #########################
    def __gt__(self, other) -> bool:
        return not self.__le__(other)# >=

    def __ge__(self, other) -> bool:
        return not self.__lt__(other)# >

    def __le__(self, other) -> bool:
        return self.wvalue <= other.wvalue# <=

    def __lt__(self, other) -> bool:
        return self.wvalue < other.wvalue# <

    def __eq__(self, other) -> bool:
        return self.wvalue == other.wvalue# ==

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)# !=
    ############################################

    def __str__(self):
        return str(self.wvalue)


def clone(ind):
    return deepcopy(ind)


def himmelblau(ind):#функция для подсчета приспасобленности
    x, y = ind
    return ((x**2 + y - 11)**2 + (x + y**2 - 7)**2)


w = 0.72984
c1 = 2.05
c2 = 2.05
BIT_LEN = 2
GENERATION = 150
SWARM_LEN = 100

Fitness.weight = -1

swarm = [Particle([random.uniform(-5, 5) for i in range(BIT_LEN)]) for t in range(SWARM_LEN)]
g_best = Particle([random.uniform(-5, 5) for i in range(BIT_LEN)])
g_best.fitness.setValue(himmelblau(g_best))

for i in range(len(swarm)):
    f = himmelblau(swarm[i])
    swarm[i].fitness.setValue(f)
    swarm[i].best = Array(swarm[i])
    swarm[i].fitbest.setValue(f)
    if swarm[i].fitness > g_best.fitness:
        g_best = clone(swarm[i])
        g_best.fitness.setValue(f)



for t in range(GENERATION):
    for i in range(SWARM_LEN):
        r1 = Array([random.random() for _ in range(BIT_LEN)])
        r2 = Array([random.random() for _ in range(BIT_LEN)])

        swarm[i].velocity = w*swarm[i].velocity + \
            (c1*r1*(swarm[i].best - swarm[i])) + \
            (c2*r2*(g_best - swarm[i]))

        swarm[i][:] = swarm[i][:] + swarm[i].velocity
        swarm[i].fitness.setValue(himmelblau(swarm[i]))

        if swarm[i].fitness > swarm[i].fitbest:
            swarm[i].best = Array(swarm[i])
            swarm[i].fitbest.setValue(himmelblau(swarm[i].best))
            if swarm[i].fitbest > g_best.fitness:
                g_best = Particle(swarm[i].best)
                g_best.fitness.setValue(himmelblau(g_best))
    
print(g_best)


"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""