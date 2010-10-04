%define DOCSTRING
"The module :mod:`pytpm.tpm` contains classes (c structures) and 
functions defined in the TPM c library.

The macros defined in the TPM c library are in the module 
:mod:`pytpm.utils`.

:Author: Prasanth Nair
:Contact: prasanthhn@gmail.com
"
%enddef 

%module(docstring=DOCSTRING) tpm


%{
  #include "tpm/v3.h"
  #include "tpm/v6.h"
  #include "tpm/m3.h"
  #include "tpm/m6.h"
  #include "tpm/vec.h"
  #include "tpm/misc.h"
  #include "tpm/times.h"
  #include "tpm/astro.h"
  #include "tpm/tpm.h"
  #include "v3Functions.h"
  #include "v6Functions.h"
  #include "m3Functions.h"
  #include "m6Functions.h"
  extern void convert(double x0, double y0, int s1, int s2,
                    double epoch, double equinox, double timetag,
                    double lon, double lat, double alt,
                    double T, double P, double H, 
                    double W,
                    double *x1, double *x2);
%}

%feature("autodoc","1");
%include "v3_swig.h"
%include "v6_swig.h"
%include "m3_swig.h"
%include "m6_swig.h"
%include "vec_swig.h"
%include "misc_swig.h"
%include "times_swig.h"
%include "astro_swig.h"
%include "tpm_swig.h"
%include "../src/v3Functions.h"
%include "../src/v6Functions.h"
%include "../src/m3Functions.h"
%include "../src/m6Functions.h"

%include "typemaps.i"

extern void convert(double x0, double y0, int s1, int s2,
                    double epoch, double equinox, double timetag,
                    double lon, double lat, double alt,
                    double T, double P, double H, 
                    double W,
                    double *OUTPUT, double *OUTPUT);

