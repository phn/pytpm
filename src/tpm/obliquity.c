/* file: $RCSfile: obliquity.c,v $
** rcsid: $Id: obliquity.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: obliquity.c,v $
** compute the mean obliquity of the ecliptic for the epoch J2000
** from Exp. Supp., 1992, p. 114
**
** return the obliquity in radians
** *******************************************************************
*/

#include "astro.h"

double
obliquity(double tdt)
{
    double T;		/* elapsed julian centuries */
    double obl;		/* obliquity */

    T = (tdt - J2000) / CJ;

    obl = 84381.448 + T * (-46.8150 + (T * (-0.00059 + (T * 0.001813))));

    obl = as2r(obl);

    return(obl);
}

double
obliquity_dot(double tdt)
{
    double T;		/* elapsed julian centuries */
    double odot;	/* obliquity */

    T = (tdt - J2000) / CJ;

    odot = -46.8150 + 2 * (T * (-0.00059 + 3 * (T * 0.001813)));

    odot = as2r(odot);

    return(odot);
}
