import numpy as np
from scipy.optimize import linprog
from nose.tools import assert_equals

def nash_equilibrium(a):
    c = [-1 for i in range(0,a.shape[1])]
    b = [1 for i in range(0,a.shape[0])]
    q = linprog(c, a, b).x
    p = linprog(b, -a.transpose(),c).x
    opt_sum = 0
    for i in p:
        opt_sum+=i
    cost = 1/opt_sum
    return (cost, p*cost, q*cost)

class TestNash:
	def test_1(self):
		matrix = np.array([
		[2, 3, 1],
		[1, 2, 5]
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 1.8
		p = np.array([0.8, 0.2])
		q = np.array([0.8, 0, 0.2])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))
	def test_2(self):
		matrix = np.array([
		[1, 3, 5, 0, -1],
		[2, 0, -1, 5, 6]
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 1.5
		p = np.array([0.5, 0.5])
		q = np.array([0.75, 0.25, 0, 0, 0])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))
	def test_3(self):
		matrix = np.array([
		[2, 4, 8, 5],
		[6, 2, 4, 6],
		[3, 2, 5, 4]
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 3.33333
		p = np.array([0.66667, 0.33333, 0])
		q = np.array([0.33333, 0.66667, 0, 0])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))
	def test_4(self):
		matrix = np.array([
		[8, 4, 7],
		[6, 5, 9],
		[7, 6, 8],
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 6
		p = np.array([0, 0, 1])
		q = np.array([0, 1, 0])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))
	def test_5(self):
		matrix = np.array([
		[4, 7, 2],
		[7, 3, 2],
		[2, 1, 8],
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 4.02941
		p = np.array([0.42647, 0.23529, 0.33824])
		q = np.array([0.35294, 0.26471, 0.38235])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))
	def test_6(self):
		matrix = np.array([
		[3, 7, 0, 9, 1, 4],
		[8, 3, 0, 5, 5, 2],
		[6, 1, 8, 3, 0, 5],
		[8, 7, 2, 0, 6, 9],
		[7, 1, 3, 6, 1, 5],
		[8, 9, 2, 4, 7, 0]
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 3.69795
		p = np.array([0.13856, 0, 0.32918, 0.16642, 0, 0.36584])
		q = np.array([0, 0, 0.24340, 0.30499, 0.28446, 0.16716])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))
	def test_7(self):
		matrix = np.array([
		[1, 3, 6, 2, 0, 3, 7, 9, 1, 4],
		[8, 0, 3, 5, 9, 7, 2, 6, 7, 7],
		[0, 1, 8, 4, 6, 5, 9, 3, 2, 0],
		[4, 8, 5, 6, 3, 2, 9, 0, 1, 6],
		[8, 3, 5, 7, 4, 0, 9, 8, 7, 1],
		[6, 3, 5, 0, 9, 6, 3, 7, 2, 8],
		[1, 2, 5, 6, 3, 4, 7, 2, 9, 0],
		[6, 8, 3, 1, 9, 2, 5, 1, 7, 3]
		])
		func_cost,func_p,func_q = nash_equilibrium(matrix)
		cost = 4.10724
		p = np.array([0, 0.29448, 0, 0.30857, 0.09912, 0.20826, 0, 0.08956])
		q = np.array([0, 0.34691, 0, 0.12837, 0, 0.24469, 0, 0.20767, 0.07237, 0])
		assert_equals(abs(func_cost - cost) < 0.00001, True)
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_p,p)), len(func_p))
		assert_equals(sum(abs(x - y) < 0.00001 for x,y in zip(func_q,q)), len(func_q))

