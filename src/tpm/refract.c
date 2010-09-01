/* file: $RCSfile: refract.c,v $
** rcsid: $Id: refract.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: refract.c,v $
** compute refraction using refraction coefficients
** for zenith distances greater than 87 degrees,
** the refraction for 87 degrees is applied.
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

#define Z_LIMIT	(87)

#define ITERATIONS	(2)

double
refract(double z, double refa, double refb, int flag)
{
    double dz;	/* refraction */
    double err;	/* iteration error */
    double tz0;	/* tangent value */
    double z0;	/* refracted (observed) zenith distance */
    double z0_last;	/* previous value */
    int i;

    /* limit the given zenith angle */
    if (z < 0) {
	z = 0;
    } else if (z > d2r(Z_LIMIT)) {
	z = d2r(Z_LIMIT);
    }

    if (flag > 0) {
	/* apply refraction */

	/* we have to iterate the refraction equation to get z0 */

	/* first guess */
	z0 = z;

	/* use newton's method to find z0 */
	for (i = 0; i < ITERATIONS; i++) {
	    z0_last = z0;
	    tz0 = tan(z0);
	    dz = tz0 * (refa + tz0 * (tz0 * refb));
	    z0 -= ((z0-z) + dz) / (1 + (refa+3*refb*tz0*tz0)/(cos(z0)*cos(z0)));
	    err = fabs(z0-z0_last);

#ifdef DEBUG
	    (void)fprintf(stdout, "refract: z0 %.15g dz %.15g z %.15g err %.15g\n",
		z0, dz, z, err);
#endif
	}
	dz *= -1.0;

    } else {
	/* remove refraction */
	z0 = z;
	tz0 = tan(z0);
	dz = tz0 * (refa + tz0 * (tz0 * refb));
	z = z0 + dz;

#ifdef DEBUG
	(void)fprintf(stdout, "refract: z0 %.15g tz0 %.15g dz %.15g z %.15g\n",
		z0, tz0, dz, z);
#endif

    }
    return(dz);
}
