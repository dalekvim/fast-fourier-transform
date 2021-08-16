import unittest

from fft.fft import fft, smallest_power_of_two_not_less_than
from fft.polynomial import Polynomial as Poly


class FFTTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.one = Poly([1])
        self.x = Poly([0, 1])
        self.x_times_two = Poly([0, 2])
        self.square = Poly([0, 0, 1])
        self.square_x_one = Poly([1, 1, 1])

    def test_degree_zero(self):
        self.assertEqual(fft(self.one), [1])

    def test_fft(self):
        self.assertEqual(fft(self.x), [1, -1])
        self.assertEqual(fft(self.x_times_two), [2, -2])
        self.assertEqual(fft(self.square), [1, -1, 1, -1])
        for i in range(4):
            self.assertAlmostEqual(fft(self.square_x_one)[i], ([3, 1j, 1, -1j])[i])

    def test_smallest_power_of_two_not_less_than(self):
        self.assertEqual(smallest_power_of_two_not_less_than(1), 1)
        self.assertEqual(smallest_power_of_two_not_less_than(2), 2)
        self.assertEqual(smallest_power_of_two_not_less_than(3), 4)
        self.assertEqual(smallest_power_of_two_not_less_than(4), 4)
        self.assertEqual(smallest_power_of_two_not_less_than(5), 8)


if __name__ == '__main__':
    unittest.main()
