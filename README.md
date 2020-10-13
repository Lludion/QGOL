# Quantum Game Of Life

## Implementation of the QGOL, as described in 1010.3120

### Representation of the objects

Config is a non-quantum configuration; it can be seen as a mutable tuple of positions (tuples).

Super is a superposition of the configurations. It can be seen as a container for a defaultdict, where the keys are the configurations and the values are the respective amplitudes.

QGOL is the Quantum Game of Life. It contains a Super object and functions to make it evolve. It keeps track of the current track to indicate where to apply the cubes to make the Config evolve.

Cube is a cube. This quite complex class contains a list of list of list of size 2x2x2 ( a cube ) and lots of fast and useful functions on it.

QCube is a container object, containing a cube and an amplitude (a complex number)

QCubes is a container object for a list of QCube objects. Notably, it comes with lots of functions to add a QCube to the list from various datatypes.

Cubes is a container object for a defaultdict of Cube objects. It adds efficiently cubes when given a position whose cube is missing, and adds the position to its rightful cube if possible.

Unit is an abstract class representing a unitary gate. Its implementation here is the unitary U (in 1010.3120), defined in obj.unit as QGOL_U.

### Further Comments

Special thanks to Pablo Arrighi and Jonathan Grattage for the creation of the QGOL.
