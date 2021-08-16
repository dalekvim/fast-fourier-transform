import unittest

from fft.polynomial import Polynomial as Poly


class PolynomialTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.empty = Poly([])
        self.zero = Poly([0])
        self.one = Poly([1])
        self.one_zero = Poly([1, 0])
        self.one_with_two_zeros = Poly([1, 0, 0])
        self.x = Poly([0, 1])
        self.square = Poly([0, 0, 1])
        self.square_then_add_x = Poly([0, 1, 1])
        self.one_to_four = Poly([1, 2, 3, 4])

    def test_add(self):
        self.assertEqual(Poly.add(self.square, self.x), self.square_then_add_x)
        self.assertEqual(Poly.add(self.x, self.square), self.square_then_add_x)

    def test_adjust(self):
        poly_1, poly_2 = Poly.adjust(self.one, self.one_zero)
        self.assertEqual(len(poly_1), len(poly_2))

    def test_are_equal(self):
        # These have exactly equal representation.
        self.assertTrue(Poly.are_equal(self.one, self.one))
        self.assertTrue(Poly.are_equal(self.x, self.x))
        self.assertTrue(Poly.are_equal(self.square, self.square))

        # These differ by trailing zero terms.
        self.assertTrue(Poly.are_equal(self.one, self.one_zero))
        self.assertTrue(Poly.are_equal(self.one, self.one_with_two_zeros))
        self.assertTrue(Poly.are_equal(self.one_zero, self.one_with_two_zeros))

        # Fixed Bug: Zero is now equal to zero.
        self.assertTrue(Poly.are_equal(self.empty, self.zero))

    def test_degree(self):
        # No trailing zeros.
        self.assertEqual(self.one.degree, 0)
        self.assertEqual(self.x.degree, 1)
        self.assertEqual(self.square.degree, 2)
        self.assertEqual(self.square_then_add_x.degree, 2)

        # Trailing zeros.
        self.assertEqual(self.one_zero.degree, 0)
        self.assertEqual(self.one_with_two_zeros.degree, 0)

        # The zero polynomial has degree -1.
        self.assertEqual(self.zero.degree, -1)

    def test_evaluation(self):
        for i in [i / 5 for i in range(-50, 50)]:
            self.assertEqual(self.zero(i), 0)
            self.assertEqual(self.one(i), 1)
            self.assertEqual(self.x(i), i)
            self.assertEqual(self.square(i), i ** 2)

    def test_evens(self):
        self.assertEqual(self.square_then_add_x.evens(), self.x)
        self.assertEqual(self.one_to_four.evens(), Poly([1, 3]))

    def test_odds(self):
        self.assertEqual(self.square_then_add_x.odds(), self.one)
        self.assertEqual(self.one_to_four.odds(), Poly([2, 4]))

    def test_strip_zeros(self):
        self.assertEqual(self.one_zero.strip_zeros(), self.one)
        self.assertEqual(self.one_with_two_zeros.strip_zeros(), self.one)

    def test_strip_zeros_list_l(self):
        self.assertEqual(Poly.strip_zeros_l([self.one_zero, self.one_with_two_zeros]), [self.one, self.one])


if __name__ == '__main__':
    unittest.main()
