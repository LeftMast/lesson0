class Horse:
    sound = 'Frrr'
    x_distance = 0

    def __init__(self):
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

    def get_pos(self):
        return self.x_distance, super().get_pos()

    def voice(self):
        return f'{super().sound}'


class Eagle:
    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0

    def fly(self, dy):
        self.y_distance += dy

    def get_pos(self):
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().fly(dy)
        super().run(dx)

    def voice(self):
        print(super().voice())


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()