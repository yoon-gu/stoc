import numpy as np
def hyperbolic_ftfs():
	a = 1.0
	Nt = 11
	Nx = 11
	f = lambda x: x**2 # initial condition
	g = lambda x: x**2 # Dirichlet boundary condition
	x = np.linspace(0.0, 1.0, Nx)
	dt = 1.0 / Nt
	dx = 1.0 / Nx
	u0 = f(x)
	u = u0 * 0
	A = np.ones((Nx,Nx))
	for j in xrange(0,Nt):
		u = A.dot(u0)
		# u0 = u
	
	return u

if __name__ == '__main__':
	print hyperbolic_ftfs()