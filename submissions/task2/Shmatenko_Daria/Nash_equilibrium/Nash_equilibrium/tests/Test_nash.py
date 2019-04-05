import unittest
import numpy as np
from Nash_equilibrium.Nash_equilibrium.code.nash import nash_equilibrium
class Test_Equilibrium(unittest.TestCase):
    def test_0(self):
        game_price, strategy1, strategy2 = nash_equilibrium([[0, 0],[0, 0]])
        self.assertAlmostEqual(game_price, 0)
        np.testing.assert_array_almost_equal([[1, 0], [1, 0]], [strategy1, strategy2])
        
    def test_1(self):
        game_price, strategy1, strategy2 = nash_equilibrium([[-5, 3, 1, 2],
                                                             [3, 1, 2, -5],
                                                             [1, 2, -5, 3],
                                                             [2, -5, 3, 1]])
        self.assertAlmostEqual(game_price, 0.25)
        np.testing.assert_array_almost_equal([[0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25]], [strategy1, strategy2])
