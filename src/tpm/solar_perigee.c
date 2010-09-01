/* file: $RCSfile: solar_perigee.c,v $
** rcsid: $Id: solar_perigee.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: solar_perigee.c,v $
** compute the mean longitude of perigee of the solar orbit
** from Exp Supp AA 1992, p 171.
**
** return the longitude in radians
** *******************************************************************
*/

#include "astro.h"

double
solar_perigee(double tdt)
{
    double T;		/* elapsed julian centuries */
    double lon;		/* longitude */

    T = (tdt - B1950) / CJ;

    lon = 1015489.951 + T * (6190.67 + (T * (1.65 + (T * 0.012))));

    lon = as2r(lon);

    return(lon);
}

double
solar_perigee_dot(double tdt)
{
    double T;		/* elapsed julian centuries */
    double ldot;

    T = (tdt - B1950) / CJ;

    ldot = 6190.67 + 2 * (T * (1.65 + 3 * (T * 0.012)));

    ldot = as2r(ldot);

    return(ldot);
}
