import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

n = 9
edges = cp.Variable(n)
#costs = cp.Variable(n, int = True)
costs  = [108, 120, 150, 150, 135, 175, 122, 148, 250]
costs = np.array(costs)
constraints = [
    edges[0] <= 1, edges[0] >=0,
    edges[1] <= 1, edges[1] >=0,
    edges[2] <= 1, edges[2] >=0,
    edges[3] <= 1, edges[3] >=0,
    edges[4] <= 1, edges[4] >=0,
    edges[5] <= 1, edges[5] >=0,
    edges[6] <= 1, edges[6] >=0,
    edges[7] <= 1, edges[7] >=0,
    edges[8] <= 1, edges[8] >=0,
    edges[0] + edges[1] + edges[2] == 1,
    edges[3] + edges[4] + edges[5] == 1,
    edges[6] + edges[7] + edges[8] == 1,
    edges[0] + edges[3] + edges[6] == 1,
    edges[1] + edges[4] + edges[7] == 1,
    edges[2] + edges[5] + edges[8] == 1,
]

obj = 0
for i in range(n):
    obj += edges[i]*costs[i]

obj = cp.Minimize(obj)

prob = cp.Problem(obj, constraints)

solver=cp.GLPK_MI
ans  = prob.solve(solver)
print(ans)
print(edges.value)
#solving a sudoku problem by framing it as an optimization problem