from utils import tf, mimotf, poles, zeros
import numpy as np

s = tf([1,0],[1])
G = mimotf([[(11*s**3 - 18*s**2 - 70*s - 50)/(s*(s + 10)*(s + 1)*(s - 5)), (s + 2)/((s + 1)*(s - 5))],
            [5*(s + 2)/((s + 1)*(s - 5)), 5*(s + 2)/((s + 1)*(s - 5))]])

print("The poles of the system are:", set(np.round(G.poles(),3)))
