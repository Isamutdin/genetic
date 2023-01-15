import random 
from func_crossing import *
from func_selection import *
from func_mutation import *
from tool import *
from functools import partial

def generate_chromosome():
    return [random.uniform(-5, 5) for i in range(2)]

def himmelblau(ind):
    x, y = ind
    return ((x**2 + y - 11)**2 + (x + y**2 - 7)**2)

Fitness.weight = -1

creator_chromosome = partial(generate_chromosome)

creator_individ = partial(generate_iter, Individ, creator_chromosome)

creator_population = partial(generate_repeat, list, 100, creator_individ)

population = creator_population()

for ind in population:
    ind.fitness.setValue(himmelblau(ind))


select =  partial(tournamentSel, tournsize=3)
crossover = partial(crossBlend, alpha=0.5)
mutation = partial(mutExchangeIndexes, chance=0.1)

print(max(classicGA(population, himmelblau, select, crossover, mutation, 0.9, 0.1, 50), key=attrgetter('fitness')))