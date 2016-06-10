from __future__ import print_function
import sympy
import utils

s = utils.tf([1, 0], 1)
M = utils.mimotf([[(s - 1) * (s + 2), 0, (s - 1) ** 2],
                   [-(s + 1) * (s + 2), (s - 1) * (s + 1), (s - 1) * (s + 1)]])
G = 1/((s + 1)*(s + 2)*(s - 1)) * M
print("The poles of the system are = ", G.poles())
