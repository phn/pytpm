from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import glob
import os

# While developing code, I do not want to re-build the tpm library
# every time I make changes to source code. So instead of compiling
# Cython and TPM code into a single module, link to the libtpm.a
# library in src/tpm. The latter was created from the C files in
# src/tpm. In Ubuntu, the following steps were used to generate the
# src/tpm/libtpm.a file:
#   gcc -c *.c
#   rm tpm_main.o
#   ar rcs libtpm.a *.o
#   ranlib libtpm.a
#   rm -f *.o


# No C files.
srcfiles = glob.glob("src/*.pyx")

depends = glob.glob("src/*.pxd")
depends.extend(glob.glob("src/*.pxi"))
depends.extend(glob.glob("src/tpm/*.h")) # Just in case.

include_dirs = [os.path.abspath("src/tpm")]

# TPM library and path to the library.
library_dirs = [os.path.abspath("src/tpm")]
libraries = ['tpm']

ext_modules = [Extension("pytpm.tpm", srcfiles,
                         depends = depends,                         
                         include_dirs = include_dirs,
                         library_dirs = library_dirs,
                         libraries = libraries)]

# Package structure is
# pytpm/__init__.py
# pytpm/tpm.so
# pytpm/*.py
# pytpm/*
setup(
    name = "pytpm",
    version = "0.4dev",
    cmdclass = {'build_ext': build_ext},
    packages = ['pytpm'],
    package_dir = {'pytpm': 'lib'},
    ext_modules = ext_modules)
