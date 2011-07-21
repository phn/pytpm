===================
 Code organization
===================

The code is organized as follow::

    $ tree -L 1
    .
    ├── devel-notes.rst
    ├── doc
    ├── examples
    ├── fake_pyrex
    ├── LICENSE.txt
    ├── MANIFEST.in
    ├── pytpm
    ├── README.rst
    ├── RELEASE_HOWTO.rst
    ├── setup-devel.py
    ├── setup.py
    └── src


#. The fake_pyrex directory exists so that distribute will run Cython
   on the Cython source file and generate the C extension. See
   `setup-devel.py` for more details.

#. I use distribute so that I can run `python setup-devel.py test` after
   making any changes, without having to install the package first. This is
   possible with distribute/setuptools but not with distutils.

#. To make the above possible, I have the `pytpm/` directory with all
   the contents of the module and a directory `pytpm/tests/` that
   contain the tests. The argument `test_suite` in `setup-devel.py`
   specifies this directory as its value.

   With this setup, when I type `python setup-devel.py test`, Cython is
   run on the Cython code in `src/`, then it is compiled to form the
   module which is then copied to `pytpm`. Then the tests inside the
   `pytpm.tests` sub-package is run.

#. While developing I do not want to keep compiling the C library. For
   this I created a static library of TPM in `src/tpm/libtpm.a` and
   then ask setuptools to link to this library. This is done in
   `setup-devel.py`. See it for more comments.

#. When shipping the code I want to compile the C library. Also I
   do not want Cython to run and instead the Cython generated C file
   should be directly used. This ensures that any version mismatch with
   user's Cython doesn't cause any problems. In fact the source
   distribution (sdist) does not include the Cython source code. This
   is achieved by `setup.py`.

So in short, if you want to work on the Cython code, then create a
static `libtpm.a` file in `src/tpm` and then use `setup-devel.py`. Run
`python setup-devel.py test`. This will create the Cython generated C
file. If you just want to test/install it then simply run `python
setup.py test/install`. This will use the existing Cython generated C
file and will compile all the C files in `src/tpm/`.

