import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as smts
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import r2_score


def integ(S, k=1):
    Sdiff = S.diff(periods=1).dropna()
    S1 = Sdiff.iloc[:, 0].values
    test = smts.adfuller(S1)
    if test[0] > test[4]['5%']:
        k = k + integ(Sdiff, k + 1)
        return k
    else:
        k = 1
        return k


def DFuller(DF):
    df1 = df.iloc[:, 0].values
    test = smts.adfuller(df1)
    if test[0] > test[4]['5%']:
        print('Not stationary')
        return
    else:
        print('Stationary')
        return


df = pd.read_excel('training.xlsx', index_col='Date', parse_dates=True)
df1 = df
df1.plot()
ax = plt.gca()
ax.set_title('Time series')
plt.show()

ma = df.rolling(window=12).mean()
ma.plot()
axma = plt.gca()
axma.set_title('Moving average')
plt.show()

sd = df.rolling(window=5).std()
sd.plot()
axsd = plt.gca()
axsd.set_title('Standart deviation')
plt.show()
print()

print('DF test:')
print()
DFuller(df)
print()

print('Decomposition:')
print('Additive model:')
print()
result = seasonal_decompose(df, model='additive')
result.plot()
plt.show()
print()

print('Multiplicative model:')
print()
result = seasonal_decompose(df, model='multiplicative')
result.plot()
plt.show()

d = integ(df)
dfdiff = df.diff(periods=1).dropna()

print()
print('ACF and PACF:')
print()
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dfdiff.values.squeeze(), lags=25, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dfdiff, lags=25, ax=ax2)
plt.show()

mod = sm.tsa.ARIMA(df, (0, 1, 0), freq='MS')
res = mod.fit()
print('ARIMA(0, 1, 0) - AIC = ', res.aic)
res.predict()

mod = sm.tsa.ARIMA(df, (0, 1, 1))
res = mod.fit()
print('ARIMA(0, 1, 1) - AIC = ', res.aic)

mod = sm.tsa.ARIMA(df, (0, 1, 2))
res = mod.fit()
print('ARIMA(0, 1, 2) - AIC = ', res.aic)

mod = sm.tsa.ARIMA(df, (0, 1, 3))
res = mod.fit()
print('ARIMA(0, 1, 3) - AIC = ', res.aic)

mod = sm.tsa.ARIMA(df, (1, 1, 0))
res = mod.fit()
print('ARIMA(1, 1, 0) - AIC = ', res.aic)

mod = sm.tsa.ARIMA(df, (1, 1, 1))
res = mod.fit()
print('ARIMA(1, 1, 1) - AIC = ', res.aic)

mod = sm.tsa.ARIMA(df, (1, 1, 2))
res = mod.fit()
print('ARIMA(1, 1, 2) - AIC = ', res.aic)

mod = sm.tsa.ARIMA(df, (1, 1, 3))
res = mod.fit()
print('ARIMA(1, 1, 3) - AIC = ', res.aic)
# наименьшее получили при (1, 1, 1)

optimal = sm.tsa.ARIMA(df, (1, 1, 1))
# pred = optimal.fit().predict('01.12.1990','01.12.1992')

