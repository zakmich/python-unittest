import unittest


class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("Michal Zak".split(), ["Michal", "Zak"])

    def test_case2(self):
        self.assertEqual("3.10".split("."), ["3", "10"])

    def test_case3(self):
        self.assertEqual("#".join(["sport", "gym"]), "sport#gym")

    def test_case4(self):
        self.assertTrue("Apple".islower())