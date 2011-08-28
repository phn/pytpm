"""Compare results with those from SLALIB.

Use this interactvely in iPython. Then copy files to pytpm/tests/data
so that automated tests can be performed.
"""
import math
from pyslalib import slalib
from read_data import get_ndwfs

tab = get_ndwfs()

# sla_fk54z.
# Convert FK5 J2000 coordinates, with zero-proper motion in the
# inertial FK5 frame to FK4 B1950.0 frame. These will have non-zero
# proper motion in the FK4 frame.
#raj2_rad = (math.radians(i) for i in tab['raj2'])
#decj2_rad =  (math.radians(i) for i in tab['decj2'])
#
#rab1 = []
#decb1 = []
#pmab1 = []
#pmdb1 = []
#
#for r,d in zip(raj2_rad, decj2_rad):
#    x,y,p,m = slalib.sla_fk54z(r, d, 1950.0)
#    rab1.append(math.degrees(x))
#    decb1.append(math.degrees(y))
#    # rad/trp. year to milli-arcsec per trp. year. NOT pma*cos(d).
#    pmab1.append(math.degrees(p)*3600.0*1e3)
#    # Milli-arcsec per trp. year.
#    pmdb1.append(math.degrees(m)*3600.0*1e3)
#
#with open("slalib_ndwfs_fk54z.txt","w") as f:
#    for r,d,p,m in zip(rab1, decb1, pmab1, pmdb1):
#        # The formats are all very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec. pm is in milli-arsec per year.
#        s = "%14.9f %14.9f %10.4f %10.4f\n" # 10.4 is very generous.
#        f.write(s % (r, d, p, m))

# sla_fk45z.
# Convert FK4 B1950.0 coordinates to FK5 J2000 coordinates, assuming
# that they has zero-proper motion in the latter. This requires
# correcting for the apparent proper motion induced by the rotating FK4
# frame and hence the epoch is needed.
#rab1_rad = (math.radians(i) for i in tab['rab1'])
#decb1_rad =  (math.radians(i) for i in tab['decb1'])
#
#raj2 = []
#decj2 = []
#for r,d in zip(rab1_rad, decb1_rad):
#    x,y = slalib.sla_fk45z(r, d, 1950.0)
#    raj2.append(math.degrees(x))
#    decj2.append(math.degrees(y))
#
#with open("slalib_ndwfs_fk45z.txt","w") as f:
#    for r,d in zip(raj2, decj2):
#        # The formats are all very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f\n"
#        f.write(s % (r, d))

# sla_eqecl.
# Convert J2000.0 FK5 equatorial coordinates to IAU 1980 ecliptic
# coordinates at J2000.0
#raj2 = (math.radians(i) for i in tab['raj2'])
#decj2 = (math.radians(i) for i in tab['decj2'])
# 
#ecl_lon = []
#ecl_lat = []
# 
#for r, d in zip(raj2, decj2):
#    x, y = slalib.sla_eqecl(r, d, 51544.5)
#    ecl_lon.append(math.degrees(x))
#    ecl_lat.append(math.degrees(y))
# 
#with open("slalib_ndwfs_eqecl.txt", "w") as f:
#    for i, j in zip(ecl_lon, ecl_lat):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (i, j))

# sla_ecleq.
# Convert IAU 1980 J2000 ecliptic coordinates to FK5 J2000 equatorial
# coordinates.
#ecl_lon = (math.radians(i) for i in tab['elon2'])
#ecl_lat = (math.radians(i) for i in tab['elat2'])
# 
#raj2 = []
#decj2 = []
# 
#for r, d in zip(ecl_lon, ecl_lat):
#    x, y = slalib.sla_ecleq(r, d, 51544.5)
#    raj2.append(math.degrees(x))
#    decj2.append(math.degrees(y))
# 
#with open("slalib_ndwfs_ecleq.txt", "w") as f:
#    for i, j in zip(raj2, decj2):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (i, j))

# sla_eqgal.
# Convert FK5 J2000.0 equatorial coordinates to galactic.
#raj2 = (math.radians(i) for i in tab['raj2'])
#decj2 = (math.radians(i) for i in tab['decj2'])
#
#gal_lon = []
#gal_lat = []
#
#for r, d in zip(raj2, decj2):
#    x, y = slalib.sla_eqgal(r, d)
#    gal_lon.append(math.degrees(x))
#    gal_lat.append(math.degrees(y))
#
#with open("slalib_ndwfs_eqgal.txt", "w") as f:
#    for l, b in zip(gal_lon, gal_lat):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (l, b))

#sla_galeq.
# Convert galactic coordinates to FK5 J2000 coordinates.
#gal_lon = (math.radians(i) for i in tab['glon'])
#gal_lat = (math.radians(i) for i in tab['glat'])
#
#raj2 = []
#decj2 = []
#
#for l, b in zip(gal_lon, gal_lat):
#    x, y = slalib.sla_galeq(l, b)
#    raj2.append(math.degrees(x))
#    decj2.append(math.degrees(y))
#
#with open("slalib_ndwfs_galeq.txt", "w") as f:
#    for r, d in zip(raj2, decj2):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (r, d))
