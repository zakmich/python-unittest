import unittest
from calculator.calc_simple import CalcSimple

class TestCalcSimple(unittest.TestCase):

    def setUp(self):
        self.calc = CalcSimple()
    def test_add1(self):
        self.assertEqual(self.calc.add(2, 5), 7)
        self.assertEqual(self.calc.add(-2, 5), 3)
        self.assertEqual(self.calc.add(2, -5), -3)
        self.assertEqual(self.calc.add(-2, -5), -7)