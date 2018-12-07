#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# 1
def diki(train):
	otg1diff = train.Value.diff(periods=1).dropna()
	t = sm.tsa.adfuller(otg1diff)
	print ('adf: ', t[0])
	print ('p-value: ', t[1])
	print ('Critical values: ', t[4])
	if t[1]> t[4]['5%']:
		print ('Есть единичные корни, ряд не стационарен.')
		return 1
	else:
		print ('Единичных корней нет, ряд стационарен.')
		return 0


train = pd.read_excel('training.xlsx', index_col ='Date')
test = pd.read_excel('testing.xlsx', index_col = 'Date')
train.head()
diki (train)

plt.figure(figsize=(20,10))
plt.plot(train, label='trainchik')
plt.show()





# 2
from pylab import rcParams
rcParams['figure.figsize'] = 11, 9
decomposition = sm.tsa.seasonal_decompose(train, model='additive')
fig = decomposition.plot()
print('\nСтационарность тренда:')
diki(decomposition.trend)
print('\nСтационарность сезональности:')
diki(decomposition.seasonal)
print('\nСтационарность остатка:')
diki(decomposition.resid)
plt.show()

plt.figure(figsize=(11,9))
decomposition = sm.tsa.seasonal_decompose(train, model='multiplicative')
decomposition.plot()
print('\nСтационарность тренда:')
diki(decomposition.trend)
print('\nСтационарность сезональности:')
diki(decomposition.seasonal)
print('\nСтационарность остатка:')
diki(decomposition.resid)
plt.show()


# In[ ]:




