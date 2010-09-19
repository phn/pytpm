from distutils.core import setup, Extension
import glob

srcfiles = glob.glob('src/tpm/*.c')
srcfiles.remove('src/tpm/tpm_main.c')
srcfiles.extend(['src/convert.c','src/tpm_wrap.c','src/v3Functions.c',
    'src/v6Functions.c','src/m3Functions.c', 'src/m6Functions.c'])

long_desc = """\
*pytpm* is a python interface to the Telescope Pointing Machine C
library written by Jeff Percival. The interface is generated using
the SWIG_ application.

The python library can be used to call most of the functions in the
TPM library, except the functions/macros that interact directly with
vectors and matrices.

A covenience function, *convert*, is provided for calling the TPM code
to perform coordinate conversions. This function is an interface to a
function of the same name provided in the file *convert.c*.
"""
setup(
        name = 'pytpm',
        version = '0.1',
        description = 'Python interface to the TPM astrometry library.',
        long_description = long_desc,
        license = 'BSD',
        author = 'Prasanth H. Nair',
        author_email = 'oneaufs@gmail.com',
        url = 'http://github.com/phn/pytpm',
        classifiers = [
          'Development Status :: 6 - Mature',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Astronomy',
          'License :: OSI Approved :: BSD License',
          ],
        packages = ['pytpm'],
        package_dir = { 'pytpm': 'lib'},
        ext_modules = [
            Extension('pytpm._tpm',
                srcfiles, include_dirs = ['src/tpm'])],
    )

