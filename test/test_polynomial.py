import unittest

from fft.polynomial import Polynomial as Poly


class PolynomialTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.one = Poly([1])
        self.one_zero = Poly([1, 0])
        self.one_with_two_zeros = Poly([1, 0, 0])
        self.x = Poly([0, 1])
        self.square = Poly([0, 0, 1])
        self.square_then_add_x = Poly([0, 1, 1])

    def test_evaluation(self):
        for i in [i / 5 for i in range(-50, 50)]:
            self.assertEqual(self.one(i), 1)
            self.assertEqual(self.x(i), i)
            self.assertEqual(self.square(i), i ** 2)

    def test_strip_zeros(self):
        self.assertEqual(self.one_zero.strip_zeros(), self.one)
        self.assertEqual(self.one_with_two_zeros.strip_zeros(), self.one)

    def test_add(self):
        self.assertEqual(Poly.add(self.square, self.x), self.square_then_add_x)
        self.assertEqual(Poly.add(self.x, self.square), self.square_then_add_x)


if __name__ == '__main__':
    unittest.main()
