# tests_12_4.py

import unittest
import logging
from runner import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("John", -5)  # Передаем отрицательное значение
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем неверный тип
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
