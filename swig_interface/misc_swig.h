/* file: $RCSfile: misc.h,v $
** rcsid: $Id: misc.h 540 2008-07-22 15:16:15Z laidler $
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
** $RCSfile: misc.h,v $ - header file for miscellaneous routines
** *******************************************************************
*/


#ifndef MISC_H

#include <stdio.h>

#define REAL	(0)
#define IMAG	(1)


#define MISC_H

#endif

extern double trapzd(double (*func)(double), double a, double b, int n);
extern double polint(double *xa, double *ya, int n, double x, double *dy);
extern double qromb(double (*func)(double), double a, double b, double
		    eps, int imax);
