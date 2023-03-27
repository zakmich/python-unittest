import unittest
from calculator.calc_simple import CalcSimple

class TestCalcSimple(unittest.TestCase):

    def test_add1(self):
        calc = CalcSimple()
        self.assertEqual(calc.add(2, 5), 7)

    def test_add2(self):
        calc = CalcSimple()
        self.assertEqual(calc.add(-2, 5), 3)

    def test_add3(self):
        calc = CalcSimple()
        self.assertEqual(calc.add(2, -5), -3)

    def test_add4(self):
        calc = CalcSimple()
        self.assertEqual(calc.add(-2, -5), -7)

