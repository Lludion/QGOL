from sys import argv

"""

Be sure to name all tests test_***(something)***

examples of correct names:
test_square
test_
test_89

"""
from img.colors import printbold

TEST_WRAPPER_LIST = []
for arg in argv:
	try:
		TEST_WRAPPER_LIST.append(int(arg))
	except ValueError:
		pass

def getz(n):
	return n in TEST_WRAPPER_LIST or not TEST_WRAPPER_LIST

def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parametrized
def qgtest(f, n):
	def aux(*xs, **kws):
		if getz(n):
			printbold(n,":",f.__doc__)
			qg = f(*xs, **kws)
			qg.cellconservation()
			return qg
	return aux

def handler(module):
	""" 
	This handler handles all tests in a given Python module.
	Be sure to name all tests test_***(something)***

	examples of correct names:
	test_square
	test_
	test_89
	"""
	tests = module.__dict__.items()
	for n,c in tests:# this executes all the activated tests
		if "test_" == n[:5]:
			try:
				c()
			except TypeError:
				pass
			except ValueError:
				pass
			except BaseException as e:
				raise(e)


