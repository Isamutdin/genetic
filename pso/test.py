from copy import deepcopy
import random

class Array(list):
    
    #Сложение#######################################################################################
    def __add__(self, other):
        result = Array()
        term = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
        for n in range(len(self)):
            result.append(self[n]+term[n])
        return result

    def __radd__(self, other):
        return self.__add__(other)
    ###############################################################################################

    #Вычитание#####################################################################################
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
    ###############################################################################################

    #Умножение#####################################################################################
    def __mul__(self, other):
        result = Array()
        other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
        for n in range(len(self)):
            result.append(other[n]*self[n])
        return result

    def __rmul__(self, other):
        return self.__mul__(other)
    ###############################################################################################


class Particle(Array):
    def __init__(self, *args):
        super().__init__(*args)
        self.velocity = Array([0 for i in range(len(self))])
        self.fitness = Fitness()
        self.best = Best([pos for pos in self])


class Best(Array):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = Fitness()
    
    def update(self, partical):
        if partical.fitness > self.fitness:
            self[:] = partical[:]
            self.fitness.setValues(partical.fitness.getValue())
            return True
        return False


class Fitness(object):

    weight = 1 

    wvalue = 0 

    def __init__(self, value=None) -> None:
        self.value = value

    def setValues(self, value) -> None:
        self.wvalue = value*self.weight
        self.value = value

    def getWValue(self):
        return self.wvalue

    def getValue(self):
        return self.value

    def delWValues(self) -> None:
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

def byta(ind):
    x, y = ind
    return ((x + 2*y - 7)**2 + (2*x + y - 5)**2)



#Инициализация#####################################################################################
fitfunc = himmelblau
w = 0.8
c1 = 3.5
c2 = 0.5
BIT_LEN = 2
LOW = -5
UP = 5
GENERATION = 100
SWARM_LEN = 100

Fitness.weight = -1

#Програмная Инициализация##########################################################################
swarm = [Particle([random.uniform(LOW, UP) for i in range(BIT_LEN)]) for t in range(SWARM_LEN)]
g_best = Best([random.uniform(LOW, UP) for i in range(BIT_LEN)])
g_best.fitness.setValues(fitfunc(g_best))

for i in range(len(swarm)):
    f = fitfunc(swarm[i])
    swarm[i].fitness.setValues(f)

    swarm[i].best = Best(swarm[i])
    swarm[i].best.fitness.setValues(f)

    g_best.update(swarm[i])
###################################################################################################

#Алгоритм##########################################################################################
for t in range(1, GENERATION+1):
    for i in range(SWARM_LEN):
        r1 = Array([random.random() for _ in range(BIT_LEN)])
        r2 = Array([random.random() for _ in range(BIT_LEN)])

        swarm[i].velocity = w*swarm[i].velocity + \
            (c1*r1*(swarm[i].best - swarm[i])) + \
            (c2*r2*(g_best - swarm[i]))

        swarm[i][:] = swarm[i][:] + swarm[i].velocity
        swarm[i].fitness.setValues(fitfunc(swarm[i]))

        if swarm[i].best.update(swarm[i]):
            g_best.update(swarm[i])

    w = (0.4/(GENERATION**2))*(t-GENERATION)**2 + 0.4
    c1 = (-3*t)/GENERATION + 3.5
    c2 = (3*t)/GENERATION + 0.5

###################################################################################################
print(g_best)


"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""