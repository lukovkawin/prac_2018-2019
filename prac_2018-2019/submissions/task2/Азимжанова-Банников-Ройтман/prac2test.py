import unittest
import prac2
from fractions import Fraction


class PracTest(unittest.TestCase):
	def test_nash_equilibrium(self):
		self.assertEqual(prac2.nash_equilibrium([[5, 1],[0, 1]]),
			[Fraction(1,1) , [Fraction(1,5), Fraction(4,5)],
			[Fraction(0,1), Fraction(1,1)]])
		self.assertEqual(prac2.nash_equilibrium([[2, 3, 1],[1, 2, 5]]),
			[Fraction(9,5), [Fraction(4,5), Fraction(1,5)],
			[Fraction(4,5), Fraction(0,1), Fraction(1,5)]])
		self.assertEqual(prac2.nash_equilibrium([[4, 0, 6, 2, 2, 1],
			[3, 8, 4, 10, 4, 4],
			[1, 2, 6, 5, 0, 0],
			[6, 6, 4, 4, 10, 3],
			[10, 4, 6, 4, 0, 9],
			[10, 7, 0, 7, 9, 8]]),
			[Fraction(151,31),
			[Fraction(0,1), Fraction(4,31), Fraction(3,31), Fraction(27,62), Fraction(21,62), Fraction(0,1)],
			[Fraction(0,1), Fraction(0,1), Fraction(257,372), Fraction(9,62), Fraction(55,372), Fraction(1,62)]])
		self.assertEqual(prac2.nash_equilibrium([[4, 2, 2], [2, 5, 0], [0, 2, 5]]),
			[Fraction(88,35), [Fraction(19,35), Fraction(6,35), Fraction(2,7)],
			[Fraction(9,35), Fraction(2,5), Fraction(12,35)]])


if __name__ == '__main__':
	unittest.main()
