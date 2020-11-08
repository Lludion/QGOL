""" Module defining various colors used in texts. """

class bcolors:
	""" Module defining various colors used in texts. """
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = CEND = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def printbold(*args):
	""" prints in bold """
	print(bcolors.BOLD,*args,bcolors.CEND)

