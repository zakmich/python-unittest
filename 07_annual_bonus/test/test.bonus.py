import unittest
from annual_bonus.bonus import AnnualBonus


class TestAnnualBonus(unittest.TestCase):

    def test_email(self):
        bon = AnnualBonus("Michal", "Zak", "", 60000, 105)
        self.assertEqual(bon.email, "michalzak@fz.pl")
