import numpy as np

def lcg(n,seed,a,m):
    """
    Generate n pseudo-random numbers using a linear congruential generator (LCG).

    X_{n+1} = (a * X_n) mod m

    Parameters:
        n (int): number of samples
        seed (int): initial value
        a (int): multiplier
        m (int): modulus

    Returns:
        np.ndarray: array of values in [0,1]
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    if m <= 0:
        raise ValueError("m must be positive")

    if seed==0:
        raise ValueError("seed cannot be equal to zero")
    
    x_i = seed
    numbers = []

    for _ in range (n):
        #X_{i+1} = (a * X_i) mod m
        x_i=(a*x_i) % m
        numbers.append(x_i/m)
    return np.array(numbers)

    