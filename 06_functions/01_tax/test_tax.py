import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_age_incorrect_data_type(self):
        self.assertRaises(TypeError, calc_tax(100, 0.1, "18"))

    def test_calc_tax_age_negative_value(self):
        self.assertRaises(ValueError, calc_tax(100, 0.1, -18))

    def test_calc_tax_age_18(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 18), 5000)

    def test_calc_tax_age_19(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 19), 12000)

