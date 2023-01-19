import random
from copy import deepcopy
from secondary_functions import *

def clone(ind):
    return deepcopy(ind)#

def generate_iter(container, generator):
    """
    :container: class
    :generator: func
    """
    return container(generator())

def generate_repeat(container, n: int, object):
    """
    :container: class
    :n: len container
    :object: func
    """
    return container(object() for i in range(n))

def classicGA(population, fitfunc, select, crossover, mutation, cxpb, mutb, generations):
    s = Statistic()
    bookeval = BookEvolution()
    
    """Классический ГА
    1.Подсчет и "установка" пригодности

    2.Запускается цикл поколение generations

        1.Проводится отбор, который полность заменяет родительскую популяцию 1к1 при этом алгоритм требуют, 
        что выбор был стохастический и возможность выбора одного и того же индивида несколько раз

        2.Клонирование т. к. из-за выбора одного и того же индивида, несколько индивидов могут ссылаться на один и тот же object

        3.Производится скрещивание с вероятностью cxpb и с вероятностью мутации mutb для формирование новой популяции

        4.Подсчет и изменение пригодности

    3.Возвращение окончательной популяции
    """
    fitneses = list(map(fitfunc, population))

    for i in range(len(population)):
        population[i].fitness.setValue(fitneses[i])

    bookeval.write(gen=0, **s.statistics(population))

    for g in range(1, generations+1):
        offspring = select(population, len(population))
        offspring = list(map(clone, offspring))

        #Скрещивание и мутация (вынести в отдельюную функцию)
        for i in range(0, len(population), 2):
            if random.random() < cxpb:
                offspring[i], offspring[i+1] = crossover(offspring[i], offspring[i+1])

        for i in range(0, len(population)):
            if random.random() < mutb:
                offspring[i] = mutation(offspring[i])
        #####################################################

        population[:] = offspring

        fitneses = list(map(fitfunc, population))

        for i in range(len(population)):
            population[i].fitness.setValue(fitneses[i])
        
        bookeval.write(gen=g, **s.statistics(population))

    return population, bookeval


class Fitness(object):

    weight = 1 #вес определяет будет ли ГА искать максимум или минимум

    wvalue = 0 #значение умноженное на вес

    def __init__(self, value=None) -> None:
        self.value = value

    def setValue(self, value) -> None:
        self.wvalue = value*self.weight #(значение) -> значение*вес
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


class Individ(list):    
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.fitness = Fitness()