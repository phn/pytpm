/* file: $RCSfile: qromb.c,v $
** rcsid: $Id: qromb.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: qromb.c,v $ - romberg rule integration
** from Numerical Recipes (1987), section 4.3, p. 114
** *******************************************************************
*/

#include <stdlib.h>
#include <math.h>
#include "misc.h"

#undef DEBUG

#define K	(5)

static double *h = NULL;
static double *s = NULL;
static int nmax = 0;

double
qromb(double (*func)(double), double a, double b, double eps, int imax)
{
    double ss = 0;
    double dss;
    int i;

    /* allocate enough storage */
    if (imax+1 > nmax) {
#ifdef DEBUG
	(void)fprintf(stdout, "qromb: malloc %d cells %d bytes\n",
		imax+1, (imax+1) * sizeof(double));
#endif
	if (h != NULL) {
	    free(h);
	}
	h = (double *)malloc((imax+1) * sizeof(double));
	if (s != NULL) {
	    free(s);
	}
	s = (double *)malloc((imax+1) * sizeof(double));

	nmax = imax+1;
    }

    h[0] = 1;

    for (i = 0; i < imax; i++) {
	s[i] = trapzd(func, a, b, i);
	if (i >= K-1) {
	    ss = polint(&h[i-(K-1)], &s[i-(K-1)], K, 0.0, &dss);
#ifdef DEBUG
	    (void)fprintf(stdout, "qromb: a %.15e b %.15e i %d ss %.15e dss %.15e eps %.15e\n",
			a, b, i, ss, dss, eps);
#endif
	    if (fabs(dss) < eps * fabs(ss)) {
		return(ss);
	    }
	}
	h[i+1] = 0.25 * h[i];
	s[i+1] = s[i];
    }

#ifdef DEBUG
    (void)fprintf(stdout, "qromb: a %.15e b %.15e i %d ss %.15e\n", a, b, i, ss);
#endif

    return(ss);
}
