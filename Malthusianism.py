import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt

T = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968]
S = [29.72, 30.61, 31.51, 32.13, 32.34, 32.85, 33.56, 34.20, 34.83]

xdata = np.array(T)
ydata = np.log(np.array(S))


def func(x, a, b):
    return a + b * x


popt, pcov = op.curve_fit(func, xdata, ydata)

plt.plot(xdata, ydata, 'ko', label='Origin Noised data')
plt.plot(xdata, func(xdata, *popt), 'r', label='Fitted curve')
plt.show()
