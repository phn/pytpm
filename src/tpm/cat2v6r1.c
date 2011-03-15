/* file: $RCSfile: cat2v6r1.c,v $
** rcsid: $Id: cat2v6r1.c,v 1.5 2003/09/03 20:19:12 jwp Exp $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without permission.
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/
static char *rcsid = "$Id: cat2v6r1.c,v 1.5 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: cat2v6r1.c,v $
** convert a standard catalog entry into a cartesian unit vector.
** unlike cat2v6u1() and cat2v6u2(), this routine returns a true
** cartesian state vector, with components in AU and AU/day.
** this algorithm uses the ES-style cat2v6u[12]() to build a unit
** vector, then scales the position and velocity components.
** the result should match cat2v6r2().
** *******************************************************************

the inputs are:
	r:	right ascension (radians)
	d:	declination (radians)
	rd:	proper motion in right ascension (arcseconds/cy)
	dd:	proper motion in declination (arcseconds/cy)
	px:	parallax in arcseconds
	rv:	radial velocity in km/s
	C:	number of days per century (tropical or julian)

** *******************************************************************
*/

#include "astro.h"

V6
cat2v6r1(double r, double d, double rd, double dd, double px, double rv, double C)
{
    V6 v6;	/* the state vector */
    double m;		/* vector modulus */

    /* get the vector the ES way, and scale it manually */
    v6 = cat2v6u2(r, d, rd, dd, px, rv, C);
    if (px > 0.001) {
	m = 1 / as2r(px);
	v6GetPos(v6) = v3scale(v6GetPos(v6), m);
	v6GetVel(v6) = v3scale(v6GetVel(v6), m*as2r(1)/C);
    } else {
	m = 1e10;
	v6GetPos(v6) = v3scale(v6GetPos(v6), m);
	v6GetVel(v6) = v3scale(v6GetVel(v6), m*as2r(1)/C);
    }

    return(v6);
}
