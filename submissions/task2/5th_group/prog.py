import pprint
from scipy.optimize import linprog
import numpy as np
import sys

def nash_equilibrium(a):
	numrows = len(a)
	numcols = len(a[0])

	c1 = [1] * numrows
	c2 = [-1] * numcols

	A2 = np.asarray(a)
	A1 = -1 * np.asarray(A2.transpose())

	b1 = [-1] * numcols
	b2 = [1] * numrows

	res1 = linprog(c1, A_ub=A1, b_ub=b1)
	res2 = linprog(c2, A_ub=A2, b_ub=b2)

	v = 1/res1.fun
	print(v)

	p = [1] * numrows
	q = [1] * numcols

	p = res1.x * v
	q = res2.x * v

	print(p.tolist())
	print(q.tolist())


if len(sys.argv) == 2:
	matrix = open(sys.argv[1]).read()
else:
	print("python3 <prog_name> <file_name>")	
	sys.exit()
matrix = [item.split() for item in matrix.split('\n')[:-1]]

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		matrix[i][j] = int(matrix[i][j])

nash_equilibrium(matrix)
