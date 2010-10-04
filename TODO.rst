wrap all functions or provide call to perform coordinate conversion

DONE:
  convert, tpm and tpm.convert()

DONE:
    ADD T,P,H etc in convert.c::convert. The functions take these parameters
    but they are not used inside the function.


DONE:
  Wrap other functions; especially utility functions such as d2r etc., .


DONE:
 Add v3,v6,m3, m6 utility functions. 
 
 How to map m3.m[0][0] or v6.v[POS].v[0]? 
 Use matrix and vector functions. Do not access them directly using indices.

CANCELLED:
 write python interface to: argv2dms, argv2hms and argv2ymd in times.h
 No need for these functions.

CANCELLED:
 write interface to functions in misc.h. These are the integration functions.

 These need, as input, pointers to C functions, even if SWIG wrapping is used.
 Direct access to these are not required for regular users.

TODO:
 Missing function declarations? Commented out in SWIG headers for now.
 There are many functions with declaration, but no definitions. Ask Jeff
 Percival about these. Library functions; which means that these are not
 implemented probably because they are not needed.

