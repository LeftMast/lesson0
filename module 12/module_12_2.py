class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5  # Каждое движение увеличивает дистанцию на скорость * 0.5

    def run(self):
        self.distance += self.speed  # Каждое движение увеличивает дистанцию на скорость

    def __eq__(self, other):
        return self.name == other.name

class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            while runner.distance < self.distance:
                runner.run()  # Бегун бежит до достижения дистанции
            results[runner] = runner.distance

        # Сортируем результаты по дистанции и возвращаем
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        return {i + 1: runner.name for i, runner in enumerate(sorted_results.keys())}

import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_1(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())]
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_2(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())]
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_3(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())]
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
