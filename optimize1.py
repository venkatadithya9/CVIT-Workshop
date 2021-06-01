import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx


p = cvx.Variable()
c = cvx.Variable()

constraints = [
    p <= 5,
    c <= 12
]

prob = cvx.Problem(cvx.Maximize(11*p+28*c), constraints)

profit = prob.solve()

print(profit)

k = cvx.Variable()
s = cvx.Variable()

constraints = [
    k + s <= 5,
    3*k + 2*s <= 12
]

prob = cvx.Problem(cvx.Maximize(6*k+5*s), constraints)

profit = prob.solve()

print(profit)