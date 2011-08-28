"""
Downloaded votable of table 2, J/ApJ/641/140/table2, from
http://vizier.u-strasbg.fr/viz-bin/Cat?J/ApJ/641/140.
Optical counterparts in the NDWFS Bootes field (Brand+, 2006)

Selected cxoxb, raJ2000 and decJ2000. Then selected j2000, b1950, gal,
ecliptic coordinates computed by Vizier, in decimal degrees. 

Then ran this file.

Result is a space delimited file with columns:

raj2000, dej2000, raj200-vizier, dej2000-vizier, glon, glat,
elonj2000, elatj2000

All values are degrees.
"""
import numpy as np
from vo.table import parse_single_table
table = parse_single_table("ndwfs.vot", pedantic=False)
data = table.array

#fs = "{0:13.8f} {1:13.8f} "
#fs += "{2:10.4f} {3:10.4f} {4:13.8f} "
#fs += "{5:13.8f} {6:13.8f} {7:13.8f} {8:13.8f} "
#fs += "{9:13.8f} {10:13.8f} {11:13.8f} {12:13.8f}"

fs = "%13.8f "*10
fs = fs.rstrip()+"\n"

data_file = open("ndwfs.txt","w")

# Fields RAJ2000 and DEJ2000 are data from catalog.
# Others are calculated by Vizier.
for i in data[0::10]:
    x = i['RAJ2000'].split(" ")
    l = float(x[0])+float(x[1])/60.0+float(x[2])/3600.0
    l *= 180.0/12.0
    x = i['DEJ2000'].split(" ")
    a = float(x[0])+float(x[1])/60.0+float(x[2])/3600.0
    d = [float(j) for j in
         [l, a,
          i['_RAJ2000'], i['_DEJ2000'],
          i['_RAB1950'], i['_DEB1950'],
          i['_Glon'], i['_Glat'],
          i['_Elon2000'],i['_Elat2000']]]

    data_file.write(fs % tuple(d))
    
data_file.close()
