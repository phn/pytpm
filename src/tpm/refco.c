/* file: $RCSfile: refco.c,v $
** rcsid: $Id: refco.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: refco.c,v $
** compute the refraction coefficients A and B.
** this is the same as Pat Wallace's slalib routine sla_refco().
**
** lat:	observer's astronomical latitude
** alt:	observer's altitude above sea level in meters
** T:	ambient temperature in Kelvins
** P:	ambient pressure in millibars
** rh:	relative humidity (fractional, 0-1)
** lambda:	wavelength in micrometers
** eps:	fractional accuracy
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

void
refco(double lat, double alt, double T, double P, double rh, double lambda, double eps, double *refa, double *refb)
{
    double dz1;
    double dz2;
    double z1 = atan(1.0);
    double z2 = atan(4.0);

    dz1 = refraction(z1, lat, alt, T, P, rh, lambda, eps);
    dz2 = refraction(z2, lat, alt, T, P, rh, lambda, eps);

#ifdef DEBUG
    (void)fprintf(stdout, "refco: dz1 %.15e\n", dz1);
    (void)fprintf(stdout, "refco: dz2 %.15e\n", dz2);
#endif

    *refa = (64*dz1 - dz2)/60;
    *refb = (dz2 - 4*dz1)/60;

#ifdef DEBUG
    (void)fprintf(stdout, "refco: refa %.15e\n", *refa);
    (void)fprintf(stdout, "refco: refb %.15e\n", *refb);
#endif

    return;
}
