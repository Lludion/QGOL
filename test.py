from sys import argv

#from log.log import logg
from tst.wrappers import handler

help = """
c			: runs cube tests
g			: runs graphical tests
u (n, m ...)		: runs tests on the evolution unitary (optional arguments: numbers of the tests to run)
help			: displays this help
r nact nste r=x 	: runs randomized tests with int parameters nact, nste and r; see below
q nact nste		: same as r

r nact nste r=x runs a simulation for nste steps, where nact active cells, placed at random, are present in the initial configuration.
The tests are repeated x times. example:
r 20 r=12 30 -> 20 cells, 30 steps, test made with 12 different random initial positioning.

u used alone will display all tests of the evolution unitary.
u used with numbers between 1 and 12 will display all tests associated with those numbers.

"""

def test_all():
	if 'help' in argv:
		print(help)
	if "op" in argv:
		import tst.test_operations
		handler(tst.test_operations)
	if "gif" in argv:
		import graph.gif_generator
	if 'g' in argv:
		import tst.test_display
		tst.test_display.test_unitary()
		tst.test_display.test_show()
	if len(argv) == 1 or 'c' in argv:
		import tst.test_cube
		tst.test_cube.test_cube()
	if len(argv) == 1 or 'q' in argv or 'r' in argv:
		import tst.test_qgol
		tst.test_qgol.test_qgol()
	if len(argv) == 1 or 'u' in argv:
		import tst.test_unit
		handler(tst.test_unit)

if __name__ == '__main__':
	test_all()

