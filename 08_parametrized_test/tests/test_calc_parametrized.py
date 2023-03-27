import unittest
from calculator.calc_simple import CalcSimple


class TestCalcSimple(unittest.TestCase):

    def setUp(self):
        print("setting up")
        self.calc = CalcSimple()

    def test_add(self):
        options = [(2, 5, 7),
                   (-2, 5, 3),
                   (2, -5, -3),
                   (-2, -5, -7),
                   ]

        for x, y, result in options:
            with self.subTest(options=options):
                self.assertEqual(self.calc.add(x, y), result)
