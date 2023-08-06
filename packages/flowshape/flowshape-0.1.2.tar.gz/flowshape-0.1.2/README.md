# FlowShape
This package provides functionality for the analysis of cell shape using the spherical harmonics decomposition.
A local branch of [lie_learn](https://github.com/AMLab-Amsterdam/lie_learn) that does not depend on cython is included (spheremesh/lie_learn). 

## Dependencies
* [libigl python bindings](https://github.com/libigl/libigl-python-bindings)
* [NumPy](https://numpy.org/)
* [SciPy](https://www.scipy.org/)

Optional:
* For the [demo](./demo.ipynb), you will need [Jupyter](https://jupyter.org/install), as well as [Meshplot](https://skoch9.github.io/meshplot/tutorial/) for plotting.

## How to use
See [demo.ipynb](./demo.ipynb) for a basic example. The API consists only of functions operating on NumPy ndarrays and there are no classes. Most functions have docstrings in the source. More documentation to follow.