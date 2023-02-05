import random
from functools import partial
from newbase import Best, Particle, Fitness
from algorithms import psoAlgorithm


def himmelblau(ind):#функция для подсчета приспасобленности
    x, y = ind
    return ((x**2 + y - 11)**2 + (x + y**2 - 7)**2)

def byta(ind):
    x, y = ind
    return ((x + 2*y - 7)**2 + (2*x + y - 5)**2)


fitfunc = partial(himmelblau)
w = 0.8
c1 = 3.5
c2 = 0.5
BIT_LEN = 2
GENERATION = 100
SWARM_LEN = 100

Fitness.weight = -1

swarm = [Particle([random.uniform(-5, 5) for i in range(BIT_LEN)]) for t in range(SWARM_LEN)]
g_best = Best([random.uniform(-5, 5) for i in range(BIT_LEN)])
g_best.fitness.setValues(fitfunc(g_best))

for i in range(len(swarm)):
    f = fitfunc(swarm[i])
    swarm[i].fitness.setValues(f)

    swarm[i].best = Best(swarm[i])
    swarm[i].best.fitness.setValues(f)

    g_best.update(swarm[i])

print(psoAlgorithm(swarm, g_best, fitfunc, GENERATION, BIT_LEN, SWARM_LEN, w, c1, c2, True))

"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""