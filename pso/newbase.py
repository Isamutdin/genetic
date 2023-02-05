from copy import deepcopy
from functools import partial
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
    
    def update(self, particale):
        if particale.fitness > self.fitness:
            self[:] = particale[:]
            self.fitness.setValues(particale.fitness.getValue())
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