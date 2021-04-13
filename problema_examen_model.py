class DuplicateDataException(ValueError):
    '''exception class for duplicate entries'''
    pass
class ShoeFact():
    '''Class to track worker progress'''
    shoes = []
    workers = {}
    work_done = {}
    def __init__(self,date: str):
        self.date = date


    def __iter__(self):
        all_series = []
        for series in self.work_done.values():
            all_series.extend(series)

        return ShoeIter(all_series)


    def add_shoes_series(self,name: str ,series: list):
        '''this method allows user to add work done'''
        conflict = 0
        try:
            values = self.work_done[name]
        except KeyError:
            values = []
        if set(values).intersection(set(series)):
            raise DuplicateDataException(set(values).intersection(set(series)))
        for worker_name,worker_series in self.work_done.items():
            if set(series).intersection(set(worker_series)):
                for duplicate in set(series).intersection(set(worker_series)):
                    series.remove(duplicate)
                    self.work_done[worker_name].remove(duplicate)
                    self.workers[duplicate] = (worker_name,name)
                conflict = 1
        self.work_done[name] = series
        if conflict:
            raise ValueError(f'Conflict series: {duplicate}, Workers: {name}, {worker_name} will be raised')

class ShoeIter():
    '''Class for iterating all series'''
    def __init__(self, series: list):
        self.series = series

    def __iter__(self):
        return self

    def __next__(self):
        if not self.series:
            raise StopIteration
        else:
            return self.series.pop(0)



shoes1 = ShoeFact('04.06.2021')
shoes1.add_shoes_series('Jerry',[124,124,126])
shoes1.add_shoes_series('Jerry',[1280,125,131])
shoes1.add_shoes_series('Max',[234,235,236])
try:
    shoes1.add_shoes_series('Gigel',[234,234,278,279])
except ValueError:
    pass
print(shoes1.work_done)
with open ('file1','w') as file:
    for i in shoes1:
        file.write(str(i) + '\n')
