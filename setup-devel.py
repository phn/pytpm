#from distutils.core import setup
#from distutils.extension import Extension
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
srcfiles.remove("src/convert.pyx")

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
ext_modules.append(
        Extension("pytpm.convert", ["src/convert.pyx"],
                  depends=["src/tpm.pyx"]))

# Package structure is
# pytpm/__init__.py
# pytpm/tpm.so
# pytpm/*.py
# pytpm/tests/
# pytpm/doc/
# and so on.
setup(
    name = "PyTPM",
    version = "0.7.1",
    cmdclass = {'build_ext': build_ext},
    packages = ['pytpm','pytpm.tests'],
    test_suite = "pytpm.tests.suite",
    use_2to3 = True,
    include_package_data = True,
    package_dir = {'pytpm.tests' : 'pytpm/tests',
                   'pytpm': 'pytpm'},
    package_data = {'pytpm.tests': ['pytpm/tests/data/*.txt',
                                    'pytpm/tests/c_tests/*.txt',
                                     ],
                    'pytpm': ['LICENSE.txt', 'README.txt']},
    ext_modules = ext_modules)
