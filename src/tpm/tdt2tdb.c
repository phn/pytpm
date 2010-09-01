/* file: $RCSfile: tdt2tdb.c,v $
** rcsid: $Id: tdt2tdb.c 261 2007-10-19 19:07:02Z laidler $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/

/*
** *******************************************************************
** $RCSfile: tdt2tdb.c,v $
** convert Terrestrial Dynamical Time (TDT)
** to Barycentric Dynamical Time (TDB)
** use formulation in Astronomical Almanac, 1984, p S15
** note that g is a function of TDB julian centuries, not TDT julian centuries,
** but the error in using TDT to compute g is negligible for computing
** apparent places of stars
** *******************************************************************
*/

#include "astro.h"

double
tdt2tdb(double tdt)
{
    double T;		/* elapsed julian centuries */
    double dt;		/* (tdb - tdt) in seconds */
    double g;
    double tdb;

    T = (tdt - J2000) / 36525;
    g = d2r(357.528 + (T * 35999.050));
    dt = 0.001658 * sin(g + (0.01671 * sin(g)));
    tdb = tdt + (dt / 86400);

    return(tdb);
}
