from sys import argv

from log.log import logg

help = """
c		: runs cube tests
u (n, m ...)	: runs tests on the evolution unitary (optional arguments: numbers of the tests to run)
help		: displays this help
r nact nste	: runs randomized tests with int parameters nact & nste; see below
q nact nste	: same as r

r nact nste runs a simulation for nste steps, where nact active cells, placed at random, are present in the initial configuration.

u used alone will display all tests of the evolution unitary.
u used with numbers between 1 and 12 will display all tests associated with those numbers.

"""

def test_all():
	if 'help' in argv:
		print(help)

	if len(argv) == 1 or 'c' in argv:
		import tst.test_cube
		tst.test_cube.test_cube()
	if len(argv) == 1 or 'q' in argv or 'r' in argv:
		import tst.test_qgol
		tst.test_qgol.test_qgol()
	if len(argv) == 1 or 'u' in argv:
		import tst.test_unit
		tests = tst.test_unit.__dict__.items()
		
		for n,c in tests:# this executes all the activated tests
			try:
				c()
			except TypeError:
				pass
			except ValueError:
				pass

if __name__ == '__main__':
	test_all()

