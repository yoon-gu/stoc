import numpy as np
def bm(size, seed = None):
	if(seed):
		np.random.seed(seed)

	val = np.random.randn(size)
	return sum(val)

def sde():
	return "hello"

def bsde():
	return "hello"