import os
from distutils.core import setup
from Cython.Distutils import Extension
from Cython.Build import cythonize

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CUR_DIR, 'src')
TPM_DIR = os.path.join(SRC_DIR, 'tpm')
include_dirs = [SRC_DIR]
src_files = ["pytpm/_tpm.pyx"]

# TPM library and path to the library.
library_dirs = [os.path.expanduser("~/lib/tpm")]
libraries = ['tpm']

ext_modules = [
    Extension(
        "pytpm._tpm", src_files,
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        libraries=libraries
    )
]

setup(
    name='pytpm',
    packages=['pytpm'],
    package_dir={'pytpm': 'pytpm'},
    package_data={'pytpm': ['*.pxd', '*.pyx', '*.pxi']},
    ext_modules=cythonize(ext_modules)
)
