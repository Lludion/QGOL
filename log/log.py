import logging as logg

logg.basicConfig(filename='log/qgol.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logg.INFO)
logg.info('Logging initialized.')

def logd(func):
	"""
	Wrapper to check when a function is entered or exited - outputs as debug
	"""
	def func_wrapper(*ar,**arg):
		logg.debug("Entering function " + str(func_wrapper.__name__))
		z = func(*ar,**arg)
		logg.debug("Exiting function " + str(func_wrapper.__name__))
		return z
	func_wrapper.__name__ = func.__name__
	return func_wrapper

def logi(func):
	"""
	Wrapper to check when a function is entered or exited - outputs as an info
	"""
	def func_wrapper(*ar,**arg):
		logg.info("Entering function " + str(func_wrapper.__name__))
		z = func(*ar,**arg)
		logg.info("Exiting function " + str(func_wrapper.__name__))
		return z
	func_wrapper.__name__ = func.__name__
	return func_wrapper

def warn(*args):
	return logg.warning(args)

def debg(*args):
	return logg.debug(args)

def info(*x):
	return logg.info(x)

