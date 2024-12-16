import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Часть 1. TestSuite
suite = unittest.TestSuite()

# Добавляем тесты RunnerTest и TournamentTest в TestSuite
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

# Создаем объект класса TextTestRunner с вербальностью 2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
result = runner.run(suite)
