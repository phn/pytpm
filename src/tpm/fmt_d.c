/* file: $RCSfile: fmt_d.c,v $
** rcsid: $Id: fmt_d.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_d.c,v $ - format degrees
** *******************************************************************
*/

#include <stdio.h>
#include "times.h"

#define NBUF (5)
static char buf[NBUF][32];
static int nxtbuf = 0;

char *
fmt_d(double d)
{
    char *p;
    char sign = '+';
    double sec;
    int deg;
    int fpart;
    int ipart;
    int min;

    /* get a buffer */
    p = buf[nxtbuf++];
    nxtbuf %= NBUF;

    if (d < 0.0) {
	sign = '-';
	d = fabs(d);
    }

    deg = floor(d);
    d = 60 * (d - floor(d));
    min = floor(d);
    d = 60 * (d - floor(d));
    sec = d;

    ipart = (int)sec;
    fpart = 1e3 * (sec - ipart);

    (void)sprintf(p, "%c%02dD %02d' %02d.%03d\"",
	sign, deg, min, ipart, fpart);

    return(p);
}
