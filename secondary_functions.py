import numpy


class Statistic(object):
    def __init__(self, key=lambda ind: ind.fitness.value) -> None:
        self.key = key
        self.functions = {'mean':self.mean, 'max': self.max, 'min': self.min}
    
    def mean(self, values):
        return numpy.mean(values)

    def max(self, values):
        return numpy.max(values)

    def min(self, values):
        return numpy.min(values)

    def statistics(self, data):
        values = list(self.key(elem) for elem in data)

        entry = dict()
        for key, func in self.functions.items():
            entry[key] = func(values)

        return entry


class BookEvolution(list):

    def write(self, **infos):
        self.append(infos)

    def select(self, *names):
        if len(names) == 1:
            return [entry.get(names[0], None) for entry in self]
        return tuple([entry.get(name, None) for entry in self] for name in names)

