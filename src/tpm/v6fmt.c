/* file: $RCSfile: v6fmt.c,v $
** rcsid: $Id: v6fmt.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6fmt.c,v $ - 6-vector formatting
** *******************************************************************
*/

#include <stdio.h>
#include "vec.h"

#define NV6BUF	(5)
static char v6buf[NV6BUF][BUFSIZ];
static int nxtv6buf = 0;

char *
v6fmt(V6 v)
{
    char *p;

    /* get a buffer */
    p = v6buf[nxtv6buf++];
    nxtv6buf %= NV6BUF;

    if (v6GetType(v) == CARTESIAN) {
	(void)sprintf(p, "%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e",
		v6GetX(v),
		v6GetY(v),
		v6GetZ(v),
		v6GetXDot(v),
		v6GetYDot(v),
		v6GetZDot(v));
    } else {
	(void)sprintf(p, "%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e",
		v6GetR(v),
		v6GetAlpha(v),
		v6GetDelta(v),
		v6GetRDot(v),
		v6GetAlphaDot(v),
		v6GetDeltaDot(v));
    }

    return(p);
}
