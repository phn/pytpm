/* file: $RCSfile: fmt_h.c,v $
** rcsid: $Id: fmt_h.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_h.c,v $ - format hours
** *******************************************************************
*/

#include <stdio.h>
#include "times.h"

#define NBUF (5)
static char buf[NBUF][32];
static int nxtbuf = 0;

char *
fmt_h(double h)
{
    char *p;
    char sign = ' ';
    double sec;
    int fpart;
    int hrs;
    int ipart;
    int min;

    /* get a buffer */
    p = buf[nxtbuf++];
    nxtbuf %= NBUF;

    if (h < 0.0) {
	sign = '-';
	h = fabs(h);
    }

    hrs = floor(h);
    h = 60 * (h - floor(h));
    min = floor(h);
    h = 60 * (h - floor(h));
    sec = h;

    ipart = (int)sec;
    fpart = 1e3 * (sec - ipart);

    (void)sprintf(p, "%c%02dH %02dM %02d.%03dS",
	sign, hrs, min, ipart, fpart);

    return(p);
}
