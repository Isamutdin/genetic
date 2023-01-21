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
    
    def add(self, name, func, *args, **kwargs):
        self.functions[name] = func(*args, **kwargs)

    def statistics(self, data):
        """
        1. На вход подается популяция
        2. Формируется список со значениями, получаемыми по self.key (по умолчанию вытаскивает value)
        3. Формируется словарь где будут храниться пара имя функции – функция(values)
        """
        values = list(self.key(elem) for elem in data)

        entry = dict()
        for key, func in self.functions.items():
            entry[key] = func(values)

        return entry


class BookEvolution(list):

    def write(self, **infos):
        self.append(infos)

    def get(self, *names):
        """
        на вход подаеться имена ключей в словаре
        возвращает кортеж со списками значений по ключам
        """
        if len(names) == 1:
            return tuple(entry.get(names[0], None) for entry in self)
        return tuple([entry.get(name, None) for entry in self] for name in names)

