# from copy import deepcopy
# #from numpy import random, tile
# import random


# def himmelblau(ind):#функция для подсчета приспасобленности
#     x, y = ind
#     return ((x**2 + y - 11)**2 + (x + y**2 - 7)**2)


# class Array(list):
    
#     def __add__(self, other):
#         result = Array()
#         term = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
#         for n in range(len(self)):
#             result.append(self[n]+term[n])
#         return result

#     def __radd__(self, other):
#         return self.__add__(other)

#     def __sub__(self, other):
#         result = Array()
#         other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
#         for n in range(len(self)):
#             result.append(self[n]-other[n])
#         return result

#     def __rsub__(self, other): 
#         result = Array()
#         other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
#         for n in range(len(self)):
#             result.append(other[n]-self[n])
#         return result

#     def __mul__(self, other):
#         result = Array()
#         other = other if isinstance(other, (tuple, list)) else [other for i in range(len(self))]
#         for n in range(len(self)):
#             result.append(other[n]*self[n])
#         return result

#     def __rmul__(self, other):
#         return self.__mul__(other)


# class Particle(Array):    
#     def __init__(self, *args) -> None:
#         super().__init__(*args)
#         self.fitness = Fitness()
#         self.velocity = Velocity([])
#         self.best = BestParticle(clone(self))


# class BestParticle(Array):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.fitness = Fitness()


# class Velocity(Array):
    

#     def setVelocity(self, velocity):
#         self = velocity
    
#     def getVelocity(self):
#         return self
    
#     def delVelocity(self):
#         self.velocity = 0

#     def __getitem__(self, i):
#         return self[i]
    
#     #Умножение#################################################################
#     def __mul__(self, other):
#         clonevelocity = [other*v for v in self.velocity]
#         return Array(clonevelocity)

#     def __rmul__(self, other):
#         return self.__mul__(other)
#     ###########################################################################



#     def __str__(self) -> str:
#         return str(self)


# class Fitness(object):

#     weight = 1 

#     wvalue = 0 

#     def __init__(self, value=None) -> None:
#         self.value = value

#     def setValue(self, value) -> None:
#         self.wvalue = value*self.weight
#         self.value = value

#     def getValue(self):
#         return self.wvalue

#     def delValues(self) -> None:
#         self.wvalue = 0

#     #Сравнение Fitness #########################
#     def __gt__(self, other) -> bool:
#         return not self.__le__(other)# >=

#     def __ge__(self, other) -> bool:
#         return not self.__lt__(other)# >

#     def __le__(self, other) -> bool:
#         return self.wvalue <= other.wvalue# <=

#     def __lt__(self, other) -> bool:
#         return self.wvalue < other.wvalue# <

#     def __eq__(self, other) -> bool:
#         return self.wvalue == other.wvalue# ==

#     def __ne__(self, other) -> bool:
#         return not self.__eq__(other)# !=
#     ############################################

#     def __str__(self):
#         return str(self.wvalue)


# def clone(ind):
#     return deepcopy(ind)




# Fitness.weight = -1

# w = 0.72984
# c1 = 2
# c2 = 2
# a = Velocity(5, 1)
# print(a+1)
# # swarm = [Particle([random.uniform(-5, 5) for i in range(2)]) for n in range(100)]
# # fitenss = []
# # g_best = Particle([random.uniform(-5, 5) for i in range(2)])
# # g_best.fitness.setValue(himmelblau(g_best))
# # for particle in swarm:
# #     f = himmelblau(particle)
# #     particle.fitness.setValue(f)
# #     fitenss.append(f)
# #     particle.best = BestParticle([elem for elem in particle])
# #     particle.best.fitness.setValue(f)

# #     if particle.fitness > g_best.fitness:
# #         g_best = clone(particle)
# #         g_best.fitness.setValue(himmelblau(g_best))

# # for t in range(10):
# #     for i in range(100):
# #         r1 = Particle([random.random() for _ in range(2)])
# #         r2 = Particle([random.random() for _ in range(2)])

# #         swarm[i].velocity = Velocity(2, w*swarm[i].velocity + \
# #             (c1*r1*(swarm[i].best - swarm[i])) + \
# #             (c2*r2*(g_best - swarm[i])))

# #         print(type(swarm[i].velocity))
       
# #         swarm[i] = swarm[i] + swarm[i].velocity
# #         swarm[i].fitness.setValue(himmelblau(swarm[i]))
        
# #         if swarm[i].fitness > swarm[i].best.fitness:

# #             swarm[i].best = BestParticle([elem for elem in swarm[i]])
# #             swarm[i].best.fitness.setValue(swarm[i].fitness.getValue())

# #             if swarm[i].best.fitness > g_best.fitness:
# #                 g_best = clone(swarm[i].best)
# #                 g_best.fitness.setValue(swarm[i].best.fitness.getValue())

# # print(g_best, sep="\n")


# """right answer
# (3.0; 2.0), (-2.805118; 3.131312), (-3.779310; -3.283186), (3.584458; -1.848126)
# """