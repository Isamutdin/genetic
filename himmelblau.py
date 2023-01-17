import random 
from func_crossing import *
from func_selection import *
from func_mutation import *
from tools import *
from functools import partial

BIT_LEN = 2
POPULATION_LEN = 100
CHANCE_CROSSOVER = 0.9
CHANCE_MUTATION_INDIVID = 0.1
GENERATIONS = 100 #поколения
CHANCE_MUTATION_GEN = 0.3

def generate_gen():#функция для генерации гена
    return random.uniform(-5, 5)

def himmelblau(ind):#функция для подсчета приспасобленности
    x, y = ind
    return ((x**2 + y - 11)**2 + (x + y**2 - 7)**2)

Fitness.weight = -1 #Указываем будет ли ГА искать максимум или минимум (-1 миниму, а 1 максимум)

creator_gen = partial(generate_gen)

creator_individ = partial(generate_repeat, Individ, BIT_LEN, creator_gen)

creator_population = partial(generate_repeat, list, POPULATION_LEN, creator_individ)

population = creator_population()

for ind in population:
    ind.fitness.setValue(himmelblau(ind))

select =  partial(tournamentSel, tournsize=3)
crossover = partial(crossBlend, alpha=0.5)
mutation = partial(mutExchangeIndexes, chance=CHANCE_MUTATION_GEN)

next_population = classicGA(population, himmelblau, select, crossover, mutation, 
    CHANCE_CROSSOVER, CHANCE_MUTATION_INDIVID, GENERATIONS)

print(max(next_population, key=attrgetter('fitness')), himmelblau(max(next_population, key=attrgetter('fitness'))))

"""right answer
(3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
"""