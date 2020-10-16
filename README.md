# Quantum Game Of Life

## Implementation of the QGOL, as described in [1010.3120](https://arxiv.org/abs/1010.3120 "Main ArXiv page")

### What is a Quantum Game of Life ?

Conway's Game of Life can be described in many ways. For mathematicians, it can be seen as a cellular automaton -or, more specifically, a partitioned cellular automaton (meaning that its evolution can be explained by local rules only). It can also be seen as a 0-player game, meaning that once the initial state has been specified, its grid will evolve autonomously. For computer scientists, one of its most important features is that this game is *Turing-complete*. Any computable function can be expressed in and calculated with this game.

Similarly, the Quantum Game of Life (QGOL) described [here](https://arxiv.org/pdf/1010.3120.pdf "QGOL arXiv pdf") is a grid, populated with active or inactive *quantum* cells, evolving according to a set of local rules. Likewise, it achieves quantum universality, as Hadamard, R(pi/4) and CNOT gates can be effectively implemented. This repository features a concrete implementation of this partitioned quantum cellular automaton ([QCA](https://arxiv.org/pdf/1904.12956.pdf "Quantum Cellular Automaton pdf")).

### Representation of the objects

**Config** is a non-quantum configuration; it can be seen as a mutable tuple of positions (tuples).

**Super** is a superposition of the configurations. It can be seen as a container for a defaultdict, where the keys are the configurations and the values are the respective amplitudes.

**QGOL** is the Quantum Game of Life. It contains a Super object and functions to make it evolve. It keeps track of the current track to indicate where to apply the cubes to make the Config evolve.

**Cube** is a cube. This quite complex class contains a list of list of list of size 2x2x2 ( a cube ) and lots of fast and useful functions on it.

**QCube** is a container object, containing a cube and an amplitude (a complex number)

**QCubes** is a container object for a list of QCube objects. Notably, it comes with lots of functions to add a QCube to the list from various datatypes.

**Cubes** is a container object for a defaultdict of Cube objects. It adds efficiently cubes when given a position whose cube is missing, and adds the position to its rightful cube if possible.

**Unit** is an abstract class representing a unitary gate. Its implementation here is the unitary U (in 1010.3120), defined in obj.unit as QGOL_U.

### Further Comments

Special thanks to Pablo Arrighi and Jonathan Grattage for the creation of the [QGOL](https://arxiv.org/pdf/1010.3120.pdf "QGOL arXiv pdf"). More details and explanations can be found [here](https://docs.google.com/presentation/d/1fBKEK7S0qo7wJeW9lbydZbKjFvYAzMyKeQIjaOYFTi4/edit#slide=id.g4f341a8c7f_0_184 "presentation of rules").
