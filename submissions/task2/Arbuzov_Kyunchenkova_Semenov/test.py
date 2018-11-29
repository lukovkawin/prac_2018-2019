import unittest
import task2
import numpy as np

class Test_Task_2(unittest.TestCase):
    def test_nash_equilibrium(self):

        test = np.array([[1, 4, 1], [2, 3, 4], [0, -2, 7]])
        ans = np.array([np.array([2.0]), np.array([0., 1.0, 0.]), np.array([1.0, 0., 0.])])
        print("Test 1 running...")
        for i in range(0, 2):
            self.assertEqual(task2.nash_equilibrium(test)[i].all(), ans[i].all())
        print("Test 1 success!")

        test = np.array([[1, 2, 0, 0], [2, 1, 2, 0], [0, 2, 1, 2], [0, 0, 2, 1]])
        ans = np.array([np.array([1.0]), np.array([0., 0.5, 0.5, 0.]), np.array([0.5, 0., 0., 0.5])])
        print("Test 2 running...")
        for i in range(0, 2):
            self.assertEqual(task2.nash_equilibrium(test)[i].all(), ans[i].all())
        print("Test 2 success!")
        
        test = np.array([[-1, 1], [1, -1]])
        ans = np.array([np.array([0.0]), np.array([0.5, 0.5]), np.array([0.5, 0.5])])
        print("Test 3 running...")
        for i in range(0, 2):
            self.assertEqual(task2.nash_equilibrium(test)[i].all(), ans[i].all())
        print("Test 3 success!")
        


if __name__ == '__main__':
    unittest.main()
