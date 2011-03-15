/* file: $RCSfile: eterms.c,v $
** rcsid: $Id: eterms.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: eterms.c,v $
** compute the e-terms of elliptic aberration.
** see yallop (AJ, 97, 274) and smith (AJ, 97, 265).
** *******************************************************************
*/

#include "astro.h"

V6
eterms(double ep)
{
    double dC;
    double dD;
    double ecc;		/* eccentricity */
    double lon;		/* mean longitude of solar perigee */
    double obl;		/* obliquity */
    V6 B;

    ecc = eccentricity(ep);
    obl = obliquity(ep);
    lon = solar_perigee(ep);

    dC = -as2r(IAU_KAPPA) * ecc * cos(lon) * cos(obl);
    dD = -as2r(IAU_KAPPA) * ecc * sin(lon);

#ifdef DEBUG
    (void)fprintf(stdout, "dC %20.14f\n", r2as(dC));
    (void)fprintf(stdout, "dD %20.14f\n", r2as(dD));
#endif

    B = v6init(CARTESIAN);
    v6SetX(B, -dD);
    v6SetY(B, dC);
    v6SetZ(B, dC * tan(obl));

#ifdef DEBUG
    (void)fprintf(stdout, "B %20.14f\n", r2as(v6GetX(B)));
    (void)fprintf(stdout, "B %20.14f\n", r2as(v6GetY(B)));
    (void)fprintf(stdout, "B %20.14f\n", r2as(v6GetZ(B)));
    (void)fprintf(stdout, "B %20.14f\n", r2as(v6GetXDot(B)));
    (void)fprintf(stdout, "B %20.14f\n", r2as(v6GetYDot(B)));
    (void)fprintf(stdout, "B %20.14f\n", r2as(v6GetZDot(B)));
#endif

    return(B);
}
