"""PyTPM: Python interface to TPM."""
# setup.py: does not run Cython.
from setuptools import setup, Extension
import glob
import os


# From pyephem/setup.py.
def read(*filenames):
    """Read contents from file."""
    return open(os.path.join(os.path.dirname(__file__), *filenames)).read()

# C code and Cython generated C file.
srcfiles = glob.glob("src/tpm/*.c")
srcfiles.remove("src/tpm/tpm_main.c")  # the command line program
srcfiles.append("pytpm/_tpm.c")  # Cython generate file; using setup-dev.py
depends = glob.glob("src/tpm/*.h")
include_dirs = [os.path.abspath("src")]

ext_modules = [Extension("pytpm._tpm", srcfiles, include_dirs=include_dirs,
                         depends=depends)]

import pytpm
setup(
    name="PyTPM",
    version=pytpm.__version__,
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
    packages=['pytpm'],
    use_2to3=True,
    include_package_data=True,
    package_dir={'pytpm': 'pytpm'},
    package_data={'pytpm': ['*.pxd', '*.pyx', '*.pxi']},
    ext_modules=ext_modules
)
