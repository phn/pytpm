Downloaded vot file from vizier hipparcos page for the main hipparcos
catalog. Selected, hip, ra icrs, de icrs, plx, pmra, pmdec, and then 
specified vizier calculated j2000, b1950, gal and ecl, all in degrees.
pmra = pmra*cos(de) and units of pmra and pmde is milli-arcsec/year.

hip.txt: run hip_format.py
  All coordinates: 1991.25, J2000, B1950, Gal Ecl
hip_icrs.txt: run hip_format_icrs.py
  RA_1991 DE_1991 pmra pmdec plx
