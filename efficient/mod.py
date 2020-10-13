import numba

@numba.vectorize([numba.float64(numba.complex128),numba.float32(numba.complex64)])
def probatab(x):
	return x.real**2 + x.imag**2

