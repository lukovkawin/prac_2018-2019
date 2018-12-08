# !/usr/bin/env python
#  coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sklearn.metrics as sk

from pylab import rcParams
from statsmodels.tsa.stattools import adfuller

# Reading test file
dataset = pd.read_excel('training.xlsx', index_col='Date')

# Plot of rolling statistics
# rolling mean
n = 5
rolling_mean = dataset['Value'].rolling(n).mean()
dataset['Rolling_Mean'] = rolling_mean
#  rolling std
rolling_std = dataset['Value'].rolling(n).std()
dataset['Rolling_Std'] = rolling_std

dataset.Value.plot(figsize=(15, 6))
dataset.Rolling_Mean.plot(figsize=(15, 6))
dataset.Rolling_Std.plot(figsize=(15, 6))

# Fuller test
val = dataset.Value
test = sm.tsa.adfuller(val)
print ('adf: ', test[0])
print ('p-value: ', test[1])
print ('Critical values: ', test[4])
if test[0] > test[4]['5%']:
    print ('Ряд не стационарен, т.к. есть единичные корни')
else:
    print ('Ряд стационарен, т.к. нет единичных корней')

# Оценка: Тест Дики-Фулера говорит нам о том, что ряд не стационарен,
# это также видно и на графике, т.к. у ряда есть тренд.


# Additive model
rcParams['figure.figsize'] = 12, 7
rslt = sm.tsa.seasonal_decompose(val, model='additive').plot()


# Multiplicative model
rslt = sm.tsa.seasonal_decompose(val, model='multiplicative').plot()


valdiff = val.diff(periods=1).dropna()
test = sm.tsa.adfuller(valdiff)
print ('adf: ', test[0])
print ('p-value: ', test[1])
print ('Critical values: ', test[4])
if test[0] > test[4]['5%']:
    print ('Ряд не стационарен, т.к. есть едининые корни')
else:
    print ('Ряд стационарен, т.к. нет единичных корней')

valdiff.plot(figsize=(12, 6))
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(valdiff.values.squeeze(), lags=25, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(valdiff, lags=25, ax=ax2)

% % time
# ARIMA p = 25, q = 3
mdl1 = sm.tsa.ARIMA(val.squeeze(), order=(25, 1, 3),).fit()

% % time
# ARIMA p = 1, q = 4
mdl2 = sm.tsa.ARIMA(val.squeeze(), order=(12, 1, 3),).fit()

% % time
# ARIMA p = 12, q = 3
mdl3 = sm.tsa.ARIMA(val.squeeze(), order=(1, 1, 3),).fit()

pred1 = mdl1.predict(start='1989-01-01', end='1993-12-01', typ='levels')
pred2 = mdl2.predict(start='1989-01-01', end='1993-12-01', typ='levels')
pred3 = mdl3.predict(start='1989-01-01', end='1993-12-01', typ='levels')
plt.plot(pred1, label='mdl1')
plt.plot(pred2, label='mdl2')
plt.plot(pred3, label='mdl3')
plt.legend(loc='best')

dataset_2 = pd.read_excel("testing.xlsx", index_col=0)
dataset_2.tail()

val2 = dataset_2
plt.figure(figsize=(16, 8))
plt.plot(val, label='Training')
plt.plot(val2, label='Test')
plt.plot(pred1, label='mdl1')
plt.plot(pred2, label='mdl2')
plt.plot(pred3, label='mdl3')
plt.legend(loc='best')
plt.show()

r21 = sk.r2_score(val2, pred1)
r22 = sk.r2_score(val2, pred2)
r23 = sk.r2_score(val2, pred3)
print('r2 mdl1:', r21)
print('r2 mdl2:', r22)
print('r2 mdl3:', r23)

ak1 = mdl1.aic
ak2 = mdl2.aic
ak3 = mdl3.aic
print('AIC mdl1:', ak1)
print('AIC mdl2:', ak2)
print('AIC mdl3:', ak3)
