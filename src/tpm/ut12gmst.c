/* file: $RCSfile: ut12gmst.c,v $
** rcsid: $Id: ut12gmst.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: ut12gmst.c,v $
** compute the greenwich mean sidereal time from UT1.
** return the gmst in radians (0 -> 2pi)
** *******************************************************************
*/

#include "astro.h"

double
ut12gmst(double ut1)
{
    double T;		/* elapsed julian centuries */
    double gmst;	/* greenwich mean sidereal time */

    T = (ut1 - J2000) / 36525;

    gmst = 67310.54841 + (T*(8640184.812866 + (T*(0.093104 + (T * -6.2e-6)))));

    /* convert this to hours */
    gmst /= 3600.0;

    /* pick up the final term in the expansion */
    gmst += 876600.0 * T;

    /* convert from hours to radians */
    gmst = h2r(gmst);

    /* normalize it */
    gmst = r2r(gmst);

    return(gmst);
}
