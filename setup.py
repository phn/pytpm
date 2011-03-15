from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import glob
import os

srcfiles = glob.glob("src/tpm/*.c")
# This is the command line TPM program.
srcfiles.remove("src/tpm/tpm_main.c")
srcfiles.extend(glob.glob("src/*.pyx"))

depends = glob.glob("src/*.pxd")
depends.extend(glob.glob("src/*.pxi"))
depends.extend(glob.glob("src/tpm/*.h")) # Just in case.

include_dirs = [os.path.abspath("src/tpm")]
ext_modules = [Extension("pytpm.tpm", srcfiles, include_dirs = include_dirs,
                         depends = depends)]

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
