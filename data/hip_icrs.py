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

fs = "{0:13.8f} {1:13.8} {2:10.4f} {3:10.4f} {4:13.8}\n"

f = open("hip_icrs.txt","w")
for i in data[0::100]:
    x = [j for j in i if np.isnan(j)]
    if x: continue
    f.write(fs.format(
            i['RA_ICRS_'], i['_DE_ICRS_'],
            i['pmRA'],i['pmDE'],i['Plx']
            ))
f.close()
