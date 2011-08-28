"""Conversions of positions and velocities using PyTPM.

Most of the work in these examples involve reading in the table of
HIPPARCOS data, and converting to proper units.

With table reading packages such as asciitable, asciidata and atpy, the
first step would be trivial. PyTPM does not need Numpy or te table
reading software, and hence I want to have examples that don't use
these.
"""
import csv
import math
from pytpm import tpm, convert


def get_hipdata():
    """Return data in hip_full.txt.

    The data was created with hip_full.py file. Assumes that the file
    hip_full.txt is in the current directory.

    A dictionary is returned. All positions are in radians. Proper
    motions are in arc-sec per Julian century. Parallax is in
    arc-sec. The keys are:

      ra_icrs: ICRS RA
      dec_icrs: ICRS Dec
      raj2: RA J2000
      decj2: Dec J2000
      rab1: RA B1950
      decb1: Dec B1950
      glon: Galactic longitude (epoch J2000)
      glat: Galactic latitude (epoch J2000)
      elon2: Ecliptic longitude (epoch J2000)
      elat2: Ecliptic latitude (epoch J2000)
      pma: proper motion in RA (without cos(dec) factor)
      pmd: proper motion in Dec
      px: parallax.

    """
    f = open("hip_full.txt", "r")
    s = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                   delimiter=" ", skipinitialspace=True)
    d = dict(ra_icrs=[], dec_icrs=[], px=[], pma=[], pmd=[],
             raj2=[], decj2=[], rab1=[], decb1=[], glon=[],
             glat=[], elon2=[], elat2=[])

    for i in s:
        d["ra_icrs"].append(math.radians(i[0]))
        d["dec_icrs"].append(math.radians(i[1]))
        d["raj2"].append(math.radians(i[5]))
        d["decj2"].append(math.radians(i[6]))
        d["rab1"].append(math.radians(i[7]))
        d["decb1"].append(math.radians(i[8]))
        d["glon"].append(math.radians(i[9]))
        d["glat"].append(math.radians(i[10]))
        d["elon2"].append(math.radians(i[11]))
        d["elat2"].append(math.radians(i[12]))

        # milli-arc-sec/jul yr to arc-sec per Jul. cent.
        # And take out cos in RA proper motion.
        d["pma"].append(i[3] / math.cos(d["decj2"][-1]) / 1000.0 * 100.0)
        d["pmd"].append(i[4] / 1000.0 * 100.0)

        # milli-arsec to arc-sec
        d["px"].append(i[2] / 1000.0)

    f.close()
    return d


hip_tab = get_hipdata()
# Dummy radial velocities.
rv = [0.0 for i in range(len(hip_tab['px']))]
# Create V6C vectors.
v6 = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], hip_tab['pma'],
                hip_tab['pmd'], hip_tab['px'], rv, tpm.CJ)


# FK5-FK4 conversion
def fk54():
    # Convert from FK5 equinox and epoch J2000.0 to FK4 equinox B1950, but
    # at the given epoch i.e., J2000.0.
    v6o = convert.convertv6(v6, s1=6, s2=5, epoch=tpm.J2000)

    # Apply proper motion from J2000.0 to B1950.0. Objects with zero
    # velocity in FK5 will have a fictitious proper motion in FK4.
    v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)

    # Convert V6C vectors into a list of dictionaries, each of which
    # contain the 6-D Fk4 B1950.0 coordinates.
    cat = convert.v62cat(v6o, tpm.CB)

    return cat


# Equatorial to Ecliptic
def fk5ecl():
    # FK5 equinox and epoch J2000.0, to IAU 1980 ecliptic J2000.0
    v6o = convert.convertv6(v6, s1=6, s2=3)
    # Convert V6C vectors into a list of dictionaries, each of which
    # contain the 6-D Fk4 B1950.0 coordinates.
    cat = convert.v62cat(v6o, tpm.CJ)

    return cat
