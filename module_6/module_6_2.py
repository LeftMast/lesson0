class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    change_color = False

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.change_owner = False

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        if self.change_color:
            self.change_color = False
            return f'Цвет: \033[32m{self.__color}\033[0m'
        return f'Цвет: {self.__color}'

    def get_owner(self):
        if self.change_owner:
            self.change_owner = False
            return f'Владелец: \033[32m{self.owner}\033[0m'
        return f'Владелец: {self.owner}'

    def print_info(self):
        print(f'{self.get_model()}\n'
              f'{self.get_horsepower()}\n'
              f'{self.get_color()}\n'
              f'{self.get_owner()}\n')

    def set_color(self, new_color: str):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self.__color = new_color
                self.change_color = True
                return
        print(f'\033[31mНельзя сменить цвет на {new_color}\033[0m\n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __setattr__(self, key, value):
        if key == 'owner':
            self.change_owner = True
        object.__setattr__(self, key, value)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
# Проверяем что цвета вернулись к default
vehicle1.print_info()

# Проверяем что цвета остались default при создании экземпляра
vehicle2 = Sedan('Nikita', 'Subaru impreza', 'green', 110)
vehicle2.print_info()

# Еще раз проверяем цветовое выделение измененных атрибутов
vehicle2.set_color('White')
vehicle2.owner = 'Alex'
vehicle2.print_info()