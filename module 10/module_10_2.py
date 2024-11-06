import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Всего врагов
        self.days = 0  # Количество дней сражения

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день сражения)
            self.days += 1
            self.enemies -= self.power

            # Убедимся, что количество врагов не становится отрицательным
            if self.enemies < 0:
                self.enemies = 0

            print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")


# Создание экземпляров рыцарей
knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

# Запуск потоков
knight1.start()
knight2.start()

# Ожидание завершения обоих потоков
knight1.join()
knight2.join()

print("Битвы окончены!")
