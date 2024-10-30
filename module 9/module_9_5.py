class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('щaг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start
        self.__next_step = self.start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer = self.__next_step
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        self.__next_step = self.pointer + self.step
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шaг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

try:
    iter6 = Iterator(20, 40, 0)
    for i in iter6:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)