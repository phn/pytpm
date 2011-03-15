/* file: $RCSfile: v3fmt.c,v $
** rcsid: $Id: v3fmt.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v3fmt.c,v $ - format a 3-vector
** *******************************************************************
*/

#include <stdio.h>
#include "vec.h"

#define NV3BUF	(5)
static char v3buf[NV3BUF][BUFSIZ];
static int nxtv3buf = 0;

char *
v3fmt(V3 v)
{
    char *p;

    /* get a buffer */
    p = v3buf[nxtv3buf++];
    nxtv3buf %= NV3BUF;

    if (v3GetType(v) == CARTESIAN) {
	(void)sprintf(p, "%22.15e %22.15e %22.15e",
		v3GetX(v),
		v3GetY(v),
		v3GetZ(v));
    } else {
	(void)sprintf(p, "%22.15e %22.15e %22.15e",
		v3GetR(v),
		v3GetAlpha(v),
		v3GetDelta(v));
    }

    return(p);
}
