import unittest


def area(width, height):

    if not (isinstance(width, (float, int)) and
            isinstance(height, (float, int))):
        raise TypeError("Value must be float or int type")

    if not width > 0 and height > 0:
        raise ValueError("Value must be positive")

    return width * height

# print(area(5, 10))

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, "message")

if __name__ == "__main__":
    unittest.main(verbosity=2)