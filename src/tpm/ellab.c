/* file: $RCSfile: ellab.c,v $
** rcsid: $Id: ellab.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: ellab.c,v $
** add or remove elliptic aberration
** to adjust mean catalog place to catalog place.
** *******************************************************************
*/

#include "astro.h"

V6
ellab(double tdt, V6 star, int flag)
{
    double r;		/* modulus of star vector */
    V6 e;	/* eterms */

    /* cache the modulus of the star vector */
    r = v6mod(star);

    /* make it a unit vector */
    star = v6unit(star);

    /* get the e-terms */
    e = eterms(tdt);

    if (flag > 0) {
	star = v6sum(star, e);
    } else if (flag < 0) {
	star = v6diff(star, e);
    }

    /* preserve the unit length */
    star = v6unit(star);

    /* restore the true length */
    star = v6scale(star, r);

    return(star);
}
