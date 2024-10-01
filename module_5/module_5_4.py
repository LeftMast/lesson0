class house:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return  object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for n in range(new_floor + 1):
                print(n)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, house) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        return False

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        return self

    def __lt__(self, other):
        if isinstance(other, house) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, house) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, house) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, house) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, house) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        return False

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')




h1 = house('ЖК Эльбрус', 10)
print(house.houses_history)
h2 = house('ЖК Акация', 20)
print(house.houses_history)
h3 = house('ЖК Матрёшки', 20)
print(house.houses_history)

# Удаление объектов
del h2
del h3

print(house.houses_history)
