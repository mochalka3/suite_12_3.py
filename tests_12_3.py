import unittest


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if getattr(self.__class__, 'is_frozen'):
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        self.assertEqual('run', 'run')

    @skip_if_frozen
    def test_walk(self):
        self.assertEqual('walk', 'walk')

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual('challenge', 'challenge')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual('first', 'first')

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual('second', 'second')

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertEqual('third', 'third')
