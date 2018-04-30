import sympy

x,y = symbols(x,y)

phi = (x ^ y)
psi = ((x & Not(y)) | (Not(x) & y))
mu = Equivalent(phi,psi)

satisfyable( mu )