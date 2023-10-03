
import unittest  # pragma: no cover

# Author: Bui Huu Viet Hung
# MSSV: 20020106
# Written in Python v3.10.12


class Triangle:
    def __init__(self):  # pragma: no cover
        self.x = 0
        self.y = 0
        self.z = 0

    def __init__(self, x, y, z):  # pragma: no cover

        # Type Checking
        # For the sake of simplicity, we only accounted for integer, not float
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
            raise TypeError

        # Invalid data Checking
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError

        self.x = x
        self.y = y
        self.z = z

    def get_triangle_type(self):

        arr = [self.x, self.y, self.z]
        arr.sort()

        if (arr[0] + arr[1] <= arr[2]):
            return 'Not a triangle.'

        if (arr[0]**2 + arr[1]**2 == arr[2]**2):
            return 'Right triangle.'

        if (arr[0]**2 + arr[1]**2 < arr[2]**2):
            return 'Acute triangle.'

        if (arr[0]**2 + arr[1]**2 > arr[2]**2):
            return 'Obtuse triangle.'


class TestControlFlow(unittest.TestCase):  # pragma: no cover

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        triangle = Triangle(2, 5, 1)
        self.assertEqual(triangle.get_triangle_type(), 'Not a triangle.')

    def test_2(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.get_triangle_type(), 'Right triangle.')

    def test_3(self):
        triangle = Triangle(2, 3, 4)
        self.assertEqual(triangle.get_triangle_type(), 'Acute triangle.')

    def test_4(self):
        triangle = Triangle(4, 5, 6)
        self.assertEqual(triangle.get_triangle_type(), 'Obtuse triangle.')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
