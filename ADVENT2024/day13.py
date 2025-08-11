import math
import re

import numpy as np

def solve(xa,ya ,xb, yb,targetx, targety):
    sys = np.array(
        [[xa, xb],
         [ya, yb]]
    )
    det = np.linalg.det(sys)
    if det == 0:
        return 0
    vector = np.array([targetx, targety])

    ka, kb = np.linalg.solve(sys, vector)

    return math.floor(ka*3 + kb)

#print(solve(94, 22, 34, 67, 8400, 5400))
with open('entree', 'r') as f:
    f = f.read().strip().split('\n\n')
for block in f:
    numbers = re.findall(r'-?\d+', block)
    numbers = [int(n) for n in numbers]
    solution = solution + solve(numbers)
    print(solution)