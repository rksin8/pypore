# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 05:58:13 2018

@author: ranjeet
"""


import numpy as np

from scipy.optimize import minimize_scalar


def error(w0,w1,x,y_actual):
    y_pred = w0+w1*x
    #mse = ((y_actual-y_pred)**2).mean()
    mse = sum((y_actual-y_pred)**2)
    return mse


w0=50
x = np.array([1,2,3])
y = np.array([52,54,56])

res = minimize_scalar(lambda w1: error(w0,w1,x,y), bounds=(-5,5))

print(res.x)


import numpy as np
from scipy import optimize
x0 = np.array([0.1,0.1])
fun = lambda x: 0.5 * np.exp(-x[0] * (1-x[1]))

res = optimize.minimize(fun, x0, method='Nelder-Mead') # SLSQP, BFGS
print(res)


#min   sum((ydata - f(xdata, params))**2, axis=0)

# x=[eaton_coeff, dtn] to be find using optimization


#bnds = ((0, None), (0, None), (0, None))
# bounds=((3,None),)

#bounds = [(-np.inf, np.inf) for _ in b_init] + [(-1, 1)]
