"""
Downloaded vot file from vizier hipparcos page for the main hipparcos
catalog.

http://cdsarc.u-strasbg.fr/viz-bin/Cat?cat=I%2F239&target=brief&

Table I/239/hip_main.

The Hipparcos and Tycho Catalogues (ESA 1997)

Selected, hip, ra icrs, de icrs, plx, pmra, pmdec, and then
specified vizier calculated j2000, b1950, gal and ecl, all in degrees.

Then ran this file.

Output columns are:

icrs, px, pmra, pmdec, fk5, fk4, galactic, ecliptic

all angles are in degrees, px in milli-arcsec, pmra is pmra*cos(de) in
milli-arcsec per year, pmdec is in milli-arcsec per year.
"""
import numpy as np
from vo.table import parse_single_table
table = parse_single_table("hipparcos.vot", pedantic=False)
data = table.array

#fs = "{0:13.8f} {1:13.8f} "
#fs += "{2:10.4f} {3:10.4f} {4:13.8f} "
#fs += "{5:13.8f} {6:13.8f} {7:13.8f} {8:13.8f} "
#fs += "{9:13.8f} {10:13.8f} {11:13.8f} {12:13.8f}"

fs = "%13.8f %13.8f %10.4f %10.4f %10.4f %13.8f %13.8f %13.8f %13.8f "
fs += "%13.8f %13.8f %13.8f %13.8f\n"

data_file = open("hip_full.txt", "w")
for i in data[0::100]:
    x = [j for j in i if np.isnan(j)]
    if x: continue
    d = [float(j) for j in
         [i['_RA_ICRS_'], i['_DE_ICRS_'],
          i['Plx'], i['pmRA'], i['pmDE'],
          i['_RAJ2000'], i['_DEJ2000'],
          i['_RAB1950'], i['_DEB1950'],
          i['_Glon'], i['_Glat'],
          i['_Elon2000'], i['_Elat2000']]]

    data_file.write(fs % tuple(d))

data_file.close()
