import runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты заморожены')
    def test_walk(self):
        rn = runner.Runner(name='Бегун')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты заморожены')
    def test_run(self):
        rn = runner.Runner(name='Бегун')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты заморожены')
    def test_challenge(self):
        rna = runner.Runner(name='RNA') # РНК :-)
        rnb = runner.Runner(name='RnB') # R'n'B :)
        for _ in range(10):
            rna.run()
            rnb.walk()
        self.assertNotEqual(rna.distance, rnb.distance)

if __name__ == '__main__':
    unittest.main()