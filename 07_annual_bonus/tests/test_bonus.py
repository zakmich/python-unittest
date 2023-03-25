import unittest
from annual_bonus.bonus import AnnualBonus


class TestAnnualBonus(unittest.TestCase):

    def test_email1(self):
        bon = AnnualBonus("Michal", "Zak", "", 60000, 105)
        self.assertEqual(bon.email, "michalzak@fz.pl")

    def test_email2(self):
        bon = AnnualBonus("Michal", "Zak", "", 60000, 105)
        bon.first_name = "Marcin"
        self.assertEqual(bon.email, "marcinzak@fz.pl")

    def test_email3(self):
        bon = AnnualBonus("Michal", "Zak", "", 60000, 105)
        bon.last_name = "Kaz"
        self.assertEqual(bon.email, "michalkaz@fz.pl")

    def test_email4(self):
        bon = AnnualBonus("Michal", "Zak", "", 60000, 105)
        bon.employee_id = "1"
        self.assertEqual(bon.email, "michalzak1@fz.pl")

    def test_calculate_bonus(self):
        bon = AnnualBonus("Michal", "Zak", "", 60000, 105)
        self.assertEqual(bon.calculate_bonus(), 3000)
