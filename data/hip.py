"""
Downloaded vot file from vizier hipparcos page for the main hipparcos
catalog. Selected, hip, ra icrs, de icrs, plx, pmra, pmdec, and then 
specified vizier calculated j2000, b1950, gal and ecl, all in degrees.

Then ran this file.
"""

import numpy as np
from vo.table import parse_single_table
table = parse_single_table("hipparcos.vot", pedantic=False)
data = table.array

fs = "{0:13.8f} {1:13.8} {2:13.8f} {3:13.8f} {4:13.8f} {5:13.8f} "
fs += "{6:13.8f} {7:13.8f} {8:13.8} {9:13.8}\n"

f = open("hip.txt","w")
for i in data[0::100]:
    x = [j for j in i if np.isnan(j)]
    if x: continue
    f.write(fs.format(
            i['RA_ICRS_'], i['_DE_ICRS_'],
            i['_RAJ2000'], i['_DEJ2000'],
            i['_RAB1950'], i['_DEB1950'],
            i['_Glon'], i['_Glat'],
            i['_Elon2000'],i['_Elat2000']
            ))
f.close()
