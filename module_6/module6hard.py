import math


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, sides):
        self.__r = color[0]
        self.__g = color[1]
        self.__b = color[2]
        self.__color = []
        self.__sides = []
        self.set_color(self.__r, self.__g, self.__b)
        self.set_sides(self.check_sides(sides))

    def __is_valid_color(self, r, g, b):
        for color in [r, g, b]:
            if not isinstance(color, int):
                return False
            if color < 0 or 255 < color:
                return False
        return True

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            return
        self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, __new_sides):
        if self.sides_count != len(__new_sides):
            return False
        for i in __new_sides:
            if not isinstance(i, int) or i <= 0:
                return False
        return True

    def check_sides(self, sides):
        single_sides = []
        if self.sides_count != len(sides):
            if self.sides_count == 12:
                sides = sides[0]
            for i in range(self.sides_count):
                single_sides.append(sides)
            return single_sides
        return sides

    def set_sides(self, *new_sides):
        new_sides = new_sides[0]
        sides = []
        if isinstance(new_sides, int):
            sides.append(new_sides)
        if isinstance(new_sides, tuple | list):
            sides = new_sides
        if self.__is_valid_sides(sides):
            self.__sides = []
            for side in sides:
                self.__sides.append(side)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        count = 0
        for i in self.__sides:
            count += i
        return count


class Circle(Figure):

    def __init__(self, color, *sides, sides_count=1):
        self.sides_count = sides_count
        super().__init__(color, sides)
        sides = Figure.get_sides(self)
        self.radius = sides[0] / 2 * math.pi

    def get_square(self):
        return math.pi * self.radius


class Triangle(Figure):
    def __init__(self, color, *sides, sides_count=3):
        self.sides_count = sides_count
        super().__init__(color, sides)

    def get_square(self):
        sides = Figure.get_sides(self)
        p = Figure.__len__(self) / 2
        s = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return s


class Cube(Figure):
    def __init__(self, color, *sides, sides_count=12):
        self.sides_count = sides_count
        super().__init__(color, sides)

    def get_volume(self):
        sides = Figure.get_sides(self)
        return sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((150, 35, 220), 3, 4, 5)
print(cube1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)    # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)     # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)            # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади (круга):
print(circle1.get_square())

# Проверка площади (треугольника):
print(triangle1.get_square())