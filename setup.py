# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import setup, Extension

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

srcfiles = glob.glob("src/tpm/*.c")
# This is the command line TPM program.
srcfiles.remove("src/tpm/tpm_main.c")
depends = glob.glob("src/tpm/*.h") # Just in case.
include_dirs = [os.path.abspath("src/tpm")]
try:
    from Cython.Distutils import build_ext
except ImportError, e:
    from distutils.command.build_ext import build_ext
    # No Cython; use the existing Cython generated code.
    srcfiles.append("src/pytpm.c")
    ext_modules = [Extension("pytpm.tpm", srcfiles,
                         include_dirs = include_dirs,
                         depends = depends)]
    ext_modules.append(
        Extension("pytpm.convert", ["src/convert.c"]))

else:
    # Re-build Cython C file, if *.pyx, *.pxi or *.pxd have changed.
    srcfiles.extend(glob.glob("src/*.pyx"))
    depends = glob.glob("src/*.pxd")
    depends.extend(glob.glob("src/*.pxi"))
    ext_modules = [Extension("pytpm.tpm", srcfiles,
                             include_dirs = include_dirs,
                             depends = depends)]
    ext_modules.append(
        Extension("pytpm.convert", ["src/convert.pyx"],
                  depends=["src/pytpm.pyx"]))

# pytpm, pytpm.tpm, pytpm.convert, pytpm.tests.
setup(
    name = "pytpm",
    version = "0.4dev",
    cmdclass = {'build_ext': build_ext},
    packages = ['pytpm','pytpm.tests'],
    test_suite = "pytpm.tests",
    ext_modules = ext_modules)
