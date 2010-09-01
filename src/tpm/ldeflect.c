/* file: $RCSfile: ldeflect.c,v $
** rcsid: $Id: ldeflect.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: ldeflect.c,v $
** apply GR deflection of light to a state vector.
** this is from Kaplan et al. AJ 97, 1197, eq. 14.
** *******************************************************************
*/

#include "astro.h"

V6
ldeflect(V6 s, V6 e, int flag)
{
    double cprime;
    double g1;
    double g2;
    V3 ehat;
    V3 p;
    V3 qhat;
    V3 x;	/* the deflection vector */
    V3 x1;	/* scratch */
    V3 x2;	/* scratch */

    p = v6GetPos(s);

    {
	V6 v6;
	v6 = v6sum(e, s);
	qhat = v3unit(v6GetPos(v6));
    }
    ehat = v3unit(v6GetPos(e));

    cprime = 86400.0 * (IAU_C / IAU_AU);
    g1 = (2.0 * IAU_K * IAU_K) / (cprime * cprime * v6mod(e));
    g2 = 1 + v3dot(qhat, ehat);

    /* limit the value of g2 as Patrick Wallace does:
    ** clip it at 1.0e-5 radians (~922 arcseconds)
    */
    if (g2 < 1.0e-5) {
	g2 = 1.0e-5;
    }

    x1 = v3scale(ehat, v3dot(p, qhat));
    x2 = v3scale(qhat, v3dot(p, ehat));
    x = v3scale(v3diff(x1, x2), g1/g2);

    if (flag > 0) {
	p = v3sum(p, x);
    } else if (flag < 0) {
	p = v3diff(p, x);
    }

    v6SetPos(s, p);

    return(s);
}
