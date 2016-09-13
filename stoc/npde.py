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
	initial = lambda x: x * (1-x)
	b = lambda t, x, u: x * 0 + u
	L = lambda t, x, u: x * 0 + u**2
	K = lambda t, x: 0 * t * x

	Nt = 21
	dt = 1.0 / Nt
	t = np.linspace(0.0, 1.0, Nt)

	Nx = 11
	dx = 1.0 / Nx
	x = np.linspace(0.0, 1.0, Nx)

	u0 = 0.5
	V0 = initial(x)
	V = np.zeros_like(V0)
	L_ = np.zeros(Nx)
	b_ = np.ones(Nx)
	for n in xrange(0,Nt):
		L_[1:-1] = L(t[n], x[1:-1], u0)
		b_[1:-1] = b(t[n], x[1:-1], u0)

		A = np.eye(Nx)
		for k in xrange(1,Nx-1):
			if b_[k] > 0:
				A[k,k] = -1
				A[k,k+1] = 1
			else:
				A[k,k-1] = -1
				A[k,k] = 1

		V = V0 + dt / dx * (L_ + b_ * A.dot(V0))
		V0 = V
		print V