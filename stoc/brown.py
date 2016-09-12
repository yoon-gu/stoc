import numpy as np
def bm(size, seed = None, B0 = 0, T = 1.):
	if(seed):
		np.random.seed(seed)

	dt = T / (size - 1)
	zero = np.zeros(1)
	val = np.sqrt(dt) * np.random.randn(size-1)
	val = np.insert(zero, 1, val)
	val = np.cumsum(val)

	return val

def sde():
	return "hello"

def bsde():
	return "hello"