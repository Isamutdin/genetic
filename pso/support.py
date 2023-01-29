from copy import deepcopy
from operator import attrgetter


class HallofBest(object):
    
    def __init__(self, size) -> None:
        self.size = size
        self.bests = list()

    def register(self, population):
        if (len(self.bests) == 0) and (self.size != 0):
            self.bests.insert(0, deepcopy(population[0]))
        
        for ind in population:
            if ind.fitness > self.bests[0].fitness or len(self.bests) < self.size:
                for best in self.bests:
                    if best == ind:
                        break
                else:
                    if len(self.bests) >= self.size:
                        self.bests.pop(0)
                    self.bests.append(ind)

        self.bests = sorted(self.bests, key=attrgetter('fitness'))
    
    def __str__(self) -> str:
        return str(self.bests)

    def __iter__(self):
        return iter(self.bests)