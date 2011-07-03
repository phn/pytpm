# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import setup, Extension

import sys
import glob
import os

srcfiles = glob.glob("src/tpm/*.c")
# This is the command line TPM program.
srcfiles.remove("src/tpm/tpm_main.c")
depends = glob.glob("src/tpm/*.h") # Just in case.
include_dirs = [os.path.abspath("src/tpm")]

# This setup.py does not run Cython.
srcfiles.append("src/pytpm.c")
ext_modules = [Extension("pytpm.tpm", srcfiles,
                     include_dirs = include_dirs,
                     depends = depends)]
ext_modules.append(
    Extension("pytpm.convert", ["src/convert.c"]))

setup(
    name = "pytpm",
    version = "0.6dev",
    packages = ['pytpm','pytpm.tests'],
    test_suite = "pytpm.tests",
    ext_modules = ext_modules)
