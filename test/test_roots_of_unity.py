import unittest

from fft.roots_of_unity import NthRootsOfUnity


class NthRootsOfUnityTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.roots_2 = [1, -1]
        self.calculated_roots_2 = NthRootsOfUnity(2)
        self.roots_4 = [1, 1j, -1, -1j]
        self.calculated_roots_4 = NthRootsOfUnity(4)

    def test_nth_roots_of_unity(self):
        for i in range(2):
            self.assertAlmostEqual(self.roots_2[i], self.calculated_roots_2[i])
        for i in range(4):
            self.assertAlmostEqual(self.roots_4[i], self.calculated_roots_4[i])

    def test_first_half(self):
        self.assertEqual(len(self.calculated_roots_2) // 2, len(self.calculated_roots_2.first_half()))
        self.assertEqual(len(self.calculated_roots_4) // 2, len(self.calculated_roots_4.first_half()))

        self.assertAlmostEqual(self.calculated_roots_2.first_half()[0], 1)
        for i in range(2):
            self.assertAlmostEqual(self.calculated_roots_4.first_half()[i], self.roots_4[i])

    def test_copy_roots(self):
        self.assertEqual(self.calculated_roots_2, self.calculated_roots_2.copy_roots())
        self.assertEqual(self.calculated_roots_4, self.calculated_roots_4.copy_roots())


if __name__ == '__main__':
    unittest.main()
