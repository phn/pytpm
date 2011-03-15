/* file: $RCSfile: gal2equ.c,v $
** rcsid: $Id: gal2equ.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: gal2equ.c,v $
** convert a state vector from galactic to FK4 equatorial
**
** the galactic pole is at (ra,dec) = (192.25, 27.4) degrees,
** and the longitude of the ascending node of the galactic plane
** on the equator is 33 degrees.
** the transformation is Rz(-ra) * Ry(-(90-dec)) * Rz(-(90-lon))
** *******************************************************************
*/

#include "astro.h"

V6
gal2equ(V6 v6)
{
    v6 = m3v6(m3Rz(-d2r(90-GAL_LON)), v6);
    v6 = m3v6(m3Ry(-d2r(90-GAL_DEC)), v6);
    v6 = m3v6(m3Rz(-d2r(GAL_RA)), v6);

    /* add e-terms */
    v6 = ellab(B1950, v6, 1);

    return(v6);
}
