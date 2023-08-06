# Python package for GridTools headers and CMake files

## Usage

Use the following when compiling C++ code with GridTools programmatically from Python.
Either by calling a compiler directly or by generating a CMake project and calling CMake on it.

```python
import gridtools_cpp
include_dir = gridtools_cpp.get_include_dir()   # header files can be found here
cmake_dir = gridtools_cpp.get_cmake_dir()       # cmake files can be found here
```
