import unittest
from task2 import nash_equilibrium
from task2 import read_matrix
from fractions import Fraction


sol = [(Fraction(151, 31),
        [Fraction(0, 1), Fraction(4, 31), Fraction(3, 31), Fraction(27, 62), Fraction(21, 62), Fraction(0, 1)],
        [Fraction(0, 1), Fraction(0, 1), Fraction(257, 372), Fraction(9, 62), Fraction(55, 372), Fraction(1, 62)]),
       (Fraction(6, 1),
        [Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)],
        [Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]),
       (Fraction(11, 2),
        [Fraction(1, 2), Fraction(1, 2), Fraction(0, 1), Fraction(0, 1)],
        [Fraction(0, 1), Fraction(1, 2), Fraction(0, 1), Fraction(1, 2)]),
       (Fraction(137, 34),
        [Fraction(29, 68), Fraction(4, 17), Fraction(23, 68)],
        [Fraction(6, 17), Fraction(9, 34), Fraction(13, 34)])]


class Test(unittest.TestCase):
    def test_nash_equilibrium1(self):
        matrix = read_matrix('input' + str(1))
        self.assertEqual(nash_equilibrium(matrix), sol[0])

    def test_nash_equilibrium2(self):
        matrix = read_matrix('input' + str(2))
        self.assertEqual(nash_equilibrium(matrix), sol[1])

    def test_nash_equilibrium3(self):
        matrix = read_matrix('input' + str(3))
        self.assertEqual(nash_equilibrium(matrix), sol[2])

    def test_nash_equilibrium4(self):
        matrix = read_matrix('input' + str(4))
        self.assertEqual(nash_equilibrium(matrix), sol[3])


if __name__ == "__main__":
    unittest.main()
