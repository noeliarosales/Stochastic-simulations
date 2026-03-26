import sys
import os
sys.path.append(os.path.abspath("../Src"))
from lcg import lcg
import numpy as np

def random_walk(N,seed,a,m):
    u = np.array(lcg(n=N, seed=seed, a=a, m=m))
    steps = np.where(u < 0.5, -1, 1)
    walk = np.cumsum(steps)
    walk = np.append(0, walk)
    return np.array(walk)
