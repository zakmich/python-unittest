import unittest


def area(width, height):

    if not (isinstance(width, (float, int)) and
            isinstance(height, (float, int))):
        raise TypeError("Value must be float or int type")

    if not (width > 0 and height > 0):
        raise ValueError("Value must be positive")

    return width * height

# print(area(5, 10))

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, "message")

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, "4", 5)
        self.assertRaises(TypeError, area, 5, "5")

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)

