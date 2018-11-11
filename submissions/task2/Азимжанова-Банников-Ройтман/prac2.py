import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from fractions import Fraction



def matrix_negative(a):
	res = []
	for i in range(0, len(a)):
		temp = []
		for j in range (0, len(a[i])):
			temp.append(-a[i][j])
		res.append(temp)
	return res

def matrix_t(a):
	res = []
	for i in range(0, len(a[0])):
		temp = []
		for j in range (0, len(a)):
			temp.append(a[j][i])
		res.append(temp)
	return res

def arr_mult(a, b):
	temp = []
	for i in range (0, len(a)):
		temp.append(b * a[i])
	return temp

def frac(a):
	res = []
	for i in a:
		res.append(Fraction(*i.as_integer_ratio()).limit_denominator())
	return res




# SciPy 1.1.0
def nash_equilibrium(a):
	m = len(a)
	n = len(a[0])

	cz = [1]
	bz = [-1]
	cw = [-1]
	bw = [1]
	for i in range (1, m):
		cz.append(1)
		bw.append(1)
	az = matrix_negative(matrix_t(a))


	for i in range (1, n):
		cw.append(-1)
		bz.append(-1)
	aw = a

	z_res = linprog(cz, az, bz)
	w_res = linprog(cw, aw, bw)


	z = []
	w = []
	if (z_res.success and w_res.success):
		z = z_res.x
		w = w_res.x
	else:
		print("There is no solution. Sorry. :D")

	v = 0
	for i in range (0, len(w)):
		v += w[i]
	v = 1/v

	p = arr_mult(z, v)
	q = arr_mult(w, v)

	p_res = frac(p)
	q_res = frac(q)
	v_res = Fraction(*v.as_integer_ratio()).limit_denominator()

	return [v_res, p_res, q_res]




def form_ans (cost, p_in, q_in): 
	costik = cost
	p = p_in
	q = q_in
	print("cost: ")
	print(costik) 
	print("p= ") 
	print(*p) 
	print("q= ") 
	print(*q) 
	fig = plt.figure(figsize = (10, 10)) 
	ax1 = fig.add_subplot(211) 
	ax2 = fig.add_subplot(212) 
	ax1.stem(range(1, len(p) + 1), p) 
	ax2.stem(range(1, len(q) + 1), q)




# a = [[4, 0, 6, 2, 2, 1],
# 	[3, 8, 4, 10, 4, 4],
# 	[1, 2, 6, 5, 0, 0],
# 	[6, 6, 4, 4, 10, 3],
# 	[10, 4, 6, 4, 0, 9],
# 	[10, 7, 0, 7, 9, 8]]
# b = [[2, 3, 1],
# 	[1, 2, 5]]
# c = [[5, 1],
# 	[0, 1]]
# d = [[4, 2, 2],
# 	[2, 5, 0],
# 	[0, 2, 5]]
# res = nash_equilibrium(b)
# form_ans(res[0], res[1], res[2])
