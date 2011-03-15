/* file: $RCSfile: polint.c,v $
** rcsid: $Id: polint.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: polint.c,v $ - polynomial interpolation
** from Numerical Recipes (1987), section 3.1, p. 82
** *******************************************************************
*/

#include <stdlib.h>
#include <math.h>
#include "misc.h"

static double *c = NULL;
static double *d = NULL;
static int nmax = 0;

double
polint(double *xa, double *ya, int n, double x, double *dy)
{
    double den;
    double dif;
    double dift;
    double ho;
    double hp;
    double w;
    double y;
    int i;
    int m;
    int ns;

    /* allocate enough storage */
    if (n > nmax) {
#ifdef DEBUG
	(void)fprintf(stdout, "polint: malloc %d cells\n", n);
#endif
	if (c != NULL) {
	    free(c);
	}
	c = (double *)malloc(n * sizeof(double));
	if (d != NULL) {
	    free(d);
	}
	d = (double *)malloc(n * sizeof(double));
	nmax = n;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "polint: n %d x %.15e\n", n, x);
#endif

    /* find the index of the closest table entry */
    ns = 0;
    dif = fabs(x - xa[ns]);
    for (i = 0; i < n; i++) {
	dift = fabs(x - xa[i]);
	if (dift < dif) {
	    ns = i;
	    dif = dift;
	}
	c[i] = ya[i];
	d[i] = ya[i];
    }

    /* first guess */
    y = ya[ns--];
#ifdef DEBUG
    (void)fprintf(stdout, "polint: y %.15e ns %d\n", y, ns);
#endif

    for (m = 0; m < n-1; m++) {
#ifdef DEBUG
	(void)fprintf(stdout, "polint: m %d\n", m);
#endif
	for (i = 0; i < n-m-1; i++) {
#ifdef DEBUG
	    (void)fprintf(stdout, "polint: i %d\n", i);
#endif
	    ho = xa[i] - x;
	    hp = xa[i+m+1] - x;
	    w = c[i+1] - d[i];
	    den = ho - hp;
	    den = w / den;
	    c[i] = ho * den;
	    d[i] = hp * den;
	}
	if (2*ns + 1 < n-m-2) {
	    *dy = c[ns+1];
#ifdef DEBUG
	    (void)fprintf(stdout, "polint: c ns %d dy %.15e\n", ns, *dy);
#endif
	} else {
	    *dy = d[ns--];
#ifdef DEBUG
	    (void)fprintf(stdout, "polint: d ns %d dy %.15e\n", ns, *dy);
#endif
	}
	y += *dy;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "polint: n %d x %.15e y %.15e dy %.15e\n", n, x, y, *dy);
#endif

    return(y);
}
