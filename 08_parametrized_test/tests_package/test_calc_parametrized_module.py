import unittest
from parameterized import parameterized
from calculator.calc_simple import CalcSimple


class TestCalcSimple(unittest.TestCase):

    def setUp(self):
        self.calc = CalcSimple()

    @parameterized.expand([
        ("positive", 2, 5, 7),
        ("positive", -2, 5, 3),
        ("negative", 2, -5, -3),
        ("negative", -2, -5, -7),
    ])
    def test_add(self, name, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)
