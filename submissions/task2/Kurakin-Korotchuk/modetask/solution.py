#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#преобразовываем и решаем
import numpy as np
from scipy.optimize import linprog #для решения задачи экстремальной, ищет минимум

def sol (a,minim):
    a = a + minim
    matrix1 = a
    matrix2 = (-1)*np.transpose(a)
    
    #решаем задачи лин прогр.
    result1 = linprog(np.ones(len(matrix1)), matrix2, (-1)*np.ones(len(matrix2))) #прямая задача, ищем максимум
    result2 = linprog((-1)*np.ones(len(matrix2)), matrix1, np.ones(len(matrix1))) #двойственная задача, ищет минимум
    price = 1 / result1.fun #ищем цену по линейной форме (в этом случае просто сумма коэф-ов)
    
    #находим оптимальные стратегии
    strategy1 = price * result1.x
    strategy2 = price * result2.x
    price = price - minim #для исходной игры
    
    result = np.array([price, strategy1, strategy2],object)
    
    return  result

