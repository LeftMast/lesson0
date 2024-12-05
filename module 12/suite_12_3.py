import unittest
from tests_12_3 import RunnerTest, TournamentTest

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Тесты будут выполняться

    @skip_if_frozen
    def test_challenge(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты будут пропущены

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(True)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests()