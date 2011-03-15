/* file: $RCSfile: trapzd.c,v $
** rcsid: $Id: trapzd.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: trapzd.c,v $ - trapezoidal quadrature
** from Numerical Recipes (1987), section 4.2, p. 111
** *******************************************************************
*/

#include "misc.h"

#undef DEBUG

double
trapzd(double (*func)(double), double a, double b, int n)
{
    double del;
    double sum;
    double tnm;
    double x;
    int j;
    static double s;
    static int it;

    if (n <= 0) {
	s = 0.5 * (b-a) * ((*func)(a) + (*func)(b));
	it = 1;
    } else {
	tnm = it;
	del = (b - a) / tnm;
	x = a + 0.5 * del;
	sum = 0;
	for (j = 0; j < it; j++) {
	    sum += (*func)(x);
	    x += del;
	}
	s = 0.5 * (s + (b-a)*sum/tnm);
	it *= 2;
    }
#ifdef DEBUG
    (void)fprintf(stdout, "trapzd: a %f b %f n %d s %f it %d\n",
	a, b, n, s, it);
#endif

    return(s);
}
