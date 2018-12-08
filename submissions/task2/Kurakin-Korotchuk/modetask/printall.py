#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#печать
import numpy as np
import matplotlib.pyplot as plt #для графиков

def allprint (result):
    print("значение игры= ", result[0])
    print("стратегия первого игрока = ", result[1])
    print("стратегия второго игрока = ", result[2])
    
    
    #графики
    t = np.arange (1, len(result[1])+1) #нач знач, конечное, шаг по умолч 1
    fig = plt.figure(1)
    plt.title ('Стратегия первого игрока')
    plt.ylabel('Стратегии')
    plt.xlabel('Номер стратегии')
    plt.scatter(t, result[1])
    plt.grid()
    plt.show()

    f = np.arange (1, len(result[2])+1) 
    fig = plt.figure(2)
    plt.title ('Стратегия второго игрока')
    plt.ylabel('Стратегии')
    plt.xlabel('Номер стратегии')
    plt.scatter(f, result[2])
    plt.grid()
    plt.show()

