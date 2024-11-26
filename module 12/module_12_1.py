class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5  # Каждый раз, когда бегун идет, он проходит 5 единиц

    def run(self):
        self.distance += 10  # Каждый раз, когда бегун бегает, он проходит 10 единиц


import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)  # 10 * 5 = 50

    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)  # 10 * 10 = 100

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()  # 10 * 10 = 100
            runner2.walk()  # 10 * 5 = 50
        self.assertNotEqual(runner1.distance, runner2.distance)  # 100 != 50


if __name__ == "__main__":
    unittest.main()
