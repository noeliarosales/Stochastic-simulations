import sys
import os
sys.path.append(os.path.abspath("../Src"))
from lcg import lcg
import numpy as np

def BernoulliProcess(N,p,seed,a,m):
  X_0 = np.array([0])
  u = np.array(lcg(n=N, seed=seed, a=a, m=m))
  # Simulamos N pasos
  experiment = np.where(u < p, 1, 0)

  # Sumamos los N pasos para obtener la trayectoria
  X_n=np.cumsum(experiment)

  # Introducimos el valor inicial del camino al comienzo, utilizando hstack
  X_n=np.hstack((X_0,X_n))

  return X_n
