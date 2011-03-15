/* file: $RCSfile: m3fmt.c,v $
** rcsid: $Id: m3fmt.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3fmt.c,v $ - format a 3-matrix
** *******************************************************************
*/

#include <stdio.h>
#include "vec.h"

#define NM3BUF	(5)
static char m3buf[NM3BUF][BUFSIZ];
static int nxtm3buf = 0;

char *
m3fmt(M3 m)
{
    char *p;

    /* get a buffer */
    p = m3buf[nxtm3buf++];
    nxtm3buf %= NM3BUF;

    (void)sprintf(p, "%22.15e %22.15e %22.15e",
	m3GetXX(m), m3GetXY(m), m3GetXZ(m));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e", p,
	m3GetYX(m), m3GetYY(m), m3GetYZ(m));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e", p,
	m3GetZX(m), m3GetZY(m), m3GetZZ(m));

    return(p);
}
