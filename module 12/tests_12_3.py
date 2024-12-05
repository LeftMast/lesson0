import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Тесты будут выполняться

    def test_challenge(self):
        self.assertTrue(True)

    def test_run(self):
        self.assertTrue(True)

    def test_walk(self):
        self.assertTrue(True)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты будут пропущены

    def test_first_tournament(self):
        self.assertTrue(True)

    def test_second_tournament(self):
        self.assertTrue(True)

    def test_third_tournament(self):
        self.assertTrue(True)
