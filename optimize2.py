import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
import csv

f = open('weight-height.csv', 'r')
data = csv.reader(f)
height = []
weight = []
for row in data:
    h = row[1]
    w = row[2]
    if h != 'Height':
        height.append(float(h))
    if w != 'Weight':
        weight.append(float(w))

c = cp.Variable(1)
m = cp.Variable(1)

constraints = []

prob = cp.Problem(cp.Minimize(cp.sum_squares(m*weight + c - height)), constraints)

y = prob.solve()

plt.plot(height, weight, 'c.')
ans = m.value*height + c.value
plt.plot(height, ans)
plt.grid()
plt.show()