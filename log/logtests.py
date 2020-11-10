try:
	from log.log import logg,logd,logi
except:
	from log import logg,logd,logi
	
@logi
def z(x):
	print("Z",x)

@logi
def f(x):
	print("lkjlk",x)
	z(ff)

@logi
def ff(x):
	print(f(f))

#ff(f(z))


@logi
def akayabu(tau,pi,lambdaprime):
	print(tau,pi)
	print(lambdaprime(tau))

#akayabu(akayabu,f,f)
