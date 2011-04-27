# Download Hipparcos data from
# http://vizier.u-strasbg.fr/cgi-bin/VizieR?-source=I/239/hip_main
# Get HIP, RAhms, DEdms, RA(ICRS)(RA in deg), DE(ICRS)(DE in deg),
# Plx (mas), pmRA(mas/yr; mu_alpha*cos(de)), pmDE(mas/yr),
# Also get SIMBAD computed distance, Galactic, J2000, B1950 and
# Ecl. J2000 values; positions in decimal degrees. Ouput is "|"
# separated values.
# se = """ """
import pytpm
from pytpm import tpm, convert

raj2000 = []
dej2000 = []
glat = []
glon = []

i = 1
for line in open("/home/phn/Downloads/hipparcos.tsv", "rt"):
    if i <= 40:
        i += 1
        continue
    cols = line.split("|")
    if cols[0].strip() == "":
        continue
    glon.append(float(cols[0]))
    glat.append(float(cols[1]))
    raj2000.append(float(cols[2]))
    dej2000.append(float(cols[3]))
    rab1950 = float(cols[4])
    deb1950 = float(cols[5])
    elon2000 = float(cols[6])
    elat2000 = float(cols[-1])
    rahip = float(cols[10])
    dehip = float(cols[11])
    plx = float(cols[12])
    pmra = float(cols[13])
    pmde = float(cols[14])
        


#import timeit
#    
#t= timeit.Timer(
#    'convert.convert(ra=raj2000, de=dej2000, s2=tpm.TPM_S04)',
#    se)
    
