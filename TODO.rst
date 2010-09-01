wrap all functions or provide call to perform coordinate conversion

DONE:
  convert, tpm and tpm.convert()

  convert && tpm 
    gives identical answers
  tpm.convert (without T,P, etc., in concert.c)
    with the same timetag agrees to ~0.1 seconds and ~0.1 arcsec.
    Why are these different?


DONE:
    ADD T,P,H etc in convert.c::convert. The functions take these parameters
    but they are not used inside the function.

    RA identical,Dec different by ~ 2-3".


DONE:
  Wrap other functions; especially utility functions such as d2r etc., .


TODO:
 Add v3,v6,m3, m6 utility functions. How to map m3.m[0][0] or
 v6.v[POS].v[0]?

TODO:
 Missing function declarations?
