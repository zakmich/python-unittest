import unittest
from annual_bonus.bonus import AnnualBonus


class TestAnnualBonus(unittest.TestCase):

    def setUp(self):  # setting up AnnualBonus class to self.bon instance
        print("setting up")
        self.bon = AnnualBonus("Michal", "Zak", "", 60000, 105)

    def tearDown(self):  # tearing down self.bon instance
        print("tearing down")
        del self.bon

    def test_email1(self):  # test to verify if email function returns correct value
        self.assertEqual(self.bon.email, "michalzak@fz.pl")

    def test_email2(self):  # test to verify if email function returns correct value after changing name
        self.bon.first_name = "Marcin"
        self.assertEqual(self.bon.email, "marcinzak@fz.pl")

    def test_email3(self):  # test to verify if email function returns correct value after changing surname
        self.bon.last_name = "Kaz"
        self.assertEqual(self.bon.email, "michalkaz@fz.pl")

    def test_email4(self):  # test to verify if email function returns correct value after changing employee id
        self.bon.employee_id = "1"
        self.assertEqual(self.bon.email, "michalzak1@fz.pl")

    def test_calculate_bonus1(self):  # test to verify if calculate_bonus function returns correct value
        self.assertEqual(self.bon.calculate_bonus(), 3000)

    def test_calculate_bonus2(
            self):  # test to verify if calculate_bonus function returns correct value after changing annual salary
        self.bon.annual_salary = 70000
        self.assertEqual(self.bon.calculate_bonus(), 3500)

    def test_calculate_bonus3(self):  # test to verify if calculate_bonus function returns correct value after changing annual assessment
        self.bon.annual_assessment = 107
        self.assertEqual(self.bon.calculate_bonus(), 4200)
