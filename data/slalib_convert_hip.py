# Convert HIPPARCOS data using SLALIB. The output files can then be
# used to compare with PyTPM.
import math
from pyslalib import slalib
import read_data
from read_data import get_hipdata

tab = get_hipdata()

# sla_fk524.
# Convert HIP FK5 J2000 coordinates as given by Vizier to B1950
# coordinates using SLALIB function fk524, which takes proper motion
# as well. This is NOT a transformation to HIPPARCOS frame. I just use
# the coordinates given by Vizier to compare proper motion conversions
# using PyTPM and SLALIB.
#raj = [math.radians(i) for i in tab['raj2']]
#decj = [math.radians(i) for i in tab["decj2"]]
## Milli-arcsec/Jul. year *cos(dec) into rad/Jul year.
#pmaj = [math.radians(i / 1000.0 / math.cos(j) / 3600.0)
#        for i, j in zip(tab['pma'], decj)]
#pmdj = [math.radians(i / 1000.0 / 3600.0)
#        for i in tab['pmd']]
#pxj = [i / 1000.0 for i in tab['px']]  # milli-arcsec to arc-sec.
#rvj = list(0.0 for i in range(len(pxj)))
#
#rab = []
#decb = []
#pmab = []
#pmdb = []
#pxb = []
#rvb = []
#
#for r, d, px, pa, pd, rv in zip(raj, decj, pxj, pmaj, pmdj, rvj):
#    r1, d1, pa1, pd1, px1, rv1 = slalib.sla_fk524(r, d, pa, pd, px, rv)
#    rab.append(math.degrees(r1))
#    decb.append(math.degrees(d1))
#    # rad/trop. year to milli-arcsec/trop. year.
#    pmab.append(math.degrees(pa1) * 3600.0 * 1e3)
#    pmdb.append(math.degrees(pd1) * 3600.0 * 1e3)
#    pxb.append(px1 * 1e3)  # arc-sec to milli-arc-sec
#    rvb.append(rv1)
#
#with open("slalib_hip_fk524.txt", "w") as f:
#    f.write("# RAB1950 RAJ1950 PX PMAB1950 PMDB1950 RV\n")
#    f.write(
#        "# deg deg milli-arcs milli-arcs/trop.yr milli-arcs/trop.yr km/s\n")
#    for r, d, px, pa, pd, rv in zip(rab, decb, pxb, pmab, pmdb, rvb):
#        # Formats are generous.
#        # degrees, miili-arc, milli-arcsec/trop. year, km/s.
#        s = "%14.9f %14.9f %10.4f %10.4f %10.4f %6.4f\n"
#        f.write(s % (r, d, px, pa, pd, rv))
