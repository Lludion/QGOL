try:
	from log.log import log
except:
	from log import log
	
@logd
def z(x):
	print("Z",x)

@logd
def f(x):
	print("lkjlk",x)
	z(ff)

@logd
def ff(x):
	print(f(f))

f(z)

