# tests_12_4.py

import unittest
import logging
from runner import Runner, Tournament

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_runner_initialization(self):
        try:
            runner = Runner("Вася", 10)
            logging.info('"test_runner_initialization" выполнен успешно')
        except Exception as e:
            logging.warning("Ошибка при инициализации Runner: %s", e)

        with self.assertRaises(TypeError):
            Runner(123, 10)  # Неверный тип имени

        with self.assertRaises(ValueError):
            Runner("Вася", -5)  # Неверная скорость

    def test_runner_methods(self):
        runner = Runner("Илья", 5)
        runner.run()
        self.assertEqual(runner.distance, 10)  # 5 * 2
        runner.walk()
        self.assertEqual(runner.distance, 15)  # 10 + 5

    def test_tournament(self):
        runner1 = Runner("Вася", 10)
        runner2 = Runner("Илья", 5)
        tournament = Tournament(101, runner1, runner2)

        finishers = tournament.start()
        logging.info('"test_tournament" выполнен успешно')

        self.assertIn(1, finishers)  # Убедимся, что есть финиширующий
        self.assertIn(2, finishers)  # Убедимся, что есть второй финиширующий


if __name__ == '__main__':
    unittest.main()

