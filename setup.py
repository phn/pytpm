# from distutils.core import setup
# from distutils.extension import Extension
import sys
import glob
import os

# For some reason setuptools.setup does not run Cython on *.pyx
# files and convert it into a *.c. From the discussion at
# http://www.velocityreviews.com/forums/
# t693861-cython-setuptools-not-working-with-pyx-only-with-c-files.html
# I found out that the lxml proect has created a fake_pyrex module
# that can fix this issue. The fake_pyrex module in this directory
# was copied from http://pypi.python.org/packages/source/l/lxml/
# lxml-2.3.tar.gz#md5=a245a015fd59b63e220005f263e1682a.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "fake_pyrex"))

from setuptools import setup, Extension
from Cython.Distutils import build_ext

srcfiles = glob.glob("src/tpm/*.c")
# This is the command line TPM program.
srcfiles.remove("src/tpm/tpm_main.c")
srcfiles.extend(glob.glob("src/*.pyx"))

depends = glob.glob("src/*.pxd")
depends.extend(glob.glob("src/*.pxi"))
depends.extend(glob.glob("src/tpm/*.h")) # Just in case.

include_dirs = [os.path.abspath("src/tpm")]
ext_modules = [Extension("pytpm.tpm", srcfiles,
                         include_dirs = include_dirs,
                         depends = depends)]

# Package structure is
# pytpm/__init__.py
# pytpm/tpm.so
# pytpm/*.py
# pytpm/tests/
# pytpm/doc/
# and so on.
setup(
    name = "pytpm",
    version = "0.4dev",
    cmdclass = {'build_ext': build_ext},
    packages = ['pytpm','pytpm.tests'],
    test_suite = "pytpm.tests",
    ext_modules = ext_modules)
