import random
from copy import deepcopy

def clone(ind):
    return deepcopy(ind)

def generate_iter(container, generator):
    return container(generator())

def generate_repeat(container, n: int, object):
    """
    :container: class
    :n: len container
    :object: func
    :args: аргументы функции
    """
    return container(object() for i in range(n))

def classicGA(population, fitfunc, select, crossover, mutation, cxpb, mutb, generations):

    fitneses = list(map(fitfunc, population))

    for i in range(len(population)):
        population[i].fitness.setValue(fitneses[i])

    for i in range(generations):
        offspring = select(population, len(population))
        offspring = list(map(clone, offspring))

        for i in range(0, len(population), 2):
            if random.random() < cxpb:
                offspring[i], offspring[i+1] = crossover(offspring[i], offspring[i+1])

        for i in range(0, len(population)):
            if random.random() < mutb:
                offspring[i] = mutation(offspring[i])

        population[:] = offspring

        fitneses = list(map(fitfunc, population))

        for i in range(len(population)):
            population[i].fitness.setValue(fitneses[i])

    return population



class Fitness(object):

    weight = 1 #вес определяет будет ли ГА искать максимум или минимум

    wvalue = 0 #значение умноженное на вес

    def __init__(self, values=None) -> None:
        self.values = values

    def setValue(self, value) -> None:
        self.wvalue = value*self.weight #(значение) -> значение*вес

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


class Individ(list):    
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.fitness = Fitness()

#ДОРАБОТАТЬ
"""
def generate_individ(individ, genrator):
    return individ(genrator())

def generate_populations(container, object, n: int):
    return container(object() for i in range(n))

"""




