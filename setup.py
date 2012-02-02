# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import setup, Extension

import sys
import glob
import os

srcfiles = glob.glob("src/tpm/*.c")
# This is the command line TPM program.
srcfiles.remove("src/tpm/tpm_main.c")
depends = glob.glob("src/tpm/*.h")  # Just in case.
include_dirs = [os.path.abspath("src/tpm")]

# This setup.py does not run Cython.
srcfiles.append("src/tpm.c")
ext_modules = [Extension("pytpm.tpm", srcfiles,
                     include_dirs=include_dirs,
                     depends=depends)]
ext_modules.append(
    Extension("pytpm.convert", ["src/convert.c"]))


# From pyephem/setup.py.
def read(*filenames):
    return open(os.path.join(os.path.dirname(__file__), *filenames)).read()

setup(
    name="PyTPM",
    version="0.7.1",
    description="Python interface to Telescope Pointing Machine C library.",
    long_description=read("README.rst"),
    license='BSD',
    author="Prasanth Nair",
    author_email="prasanthhn@gmail.com",
    url='https://github.com/phn/pytpm',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Astronomy',
        ],
    packages=['pytpm', 'pytpm.tests'],
    test_suite="pytpm.tests.suite",
    use_2to3=True,
    include_package_data=True,
    package_data={'pytpm.tests': ['pytpm/tests/data/*.txt',
                                    'pytpm/tests/c_tests/*.txt',
                                     ],
                    'pytpm': ['LICENSE.txt', 'README.txt']},
    ext_modules=ext_modules)
