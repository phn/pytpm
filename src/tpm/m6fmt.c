/* file: $RCSfile: m6fmt.c,v $
** rcsid: $Id: m6fmt.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6fmt.c,v $ - format a 6-matrix
** *******************************************************************
*/

#include <stdio.h>
#include "vec.h"

#define NM6BUF	(5)
static char m6buf[NM6BUF][BUFSIZ];
static int nxtm6buf = 0;

char *
m6fmt(M6 m)
{
    char *p;

    /* get a buffer */
    p = m6buf[nxtm6buf++];
    nxtm6buf %= NM6BUF;

    (void)sprintf(p, "%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e",
		m3GetXX(m6GetPP(m)), m3GetXY(m6GetPP(m)), m3GetXZ(m6GetPP(m)),
		m3GetXX(m6GetPV(m)), m3GetXY(m6GetPV(m)), m3GetXZ(m6GetPV(m)));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e", p,
		m3GetYX(m6GetPP(m)), m3GetYY(m6GetPP(m)), m3GetYZ(m6GetPP(m)),
		m3GetYX(m6GetPV(m)), m3GetYY(m6GetPV(m)), m3GetYZ(m6GetPV(m)));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e", p,
		m3GetZX(m6GetPP(m)), m3GetZY(m6GetPP(m)), m3GetZZ(m6GetPP(m)),
		m3GetZX(m6GetPV(m)), m3GetZY(m6GetPV(m)), m3GetZZ(m6GetPV(m)));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e", p,
		m3GetXX(m6GetVP(m)), m3GetXY(m6GetVP(m)), m3GetXZ(m6GetVP(m)),
		m3GetXX(m6GetVV(m)), m3GetXY(m6GetVV(m)), m3GetXZ(m6GetVV(m)));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e", p,
		m3GetYX(m6GetVP(m)), m3GetYY(m6GetVP(m)), m3GetYZ(m6GetVP(m)),
		m3GetYX(m6GetVV(m)), m3GetYY(m6GetVV(m)), m3GetYZ(m6GetVV(m)));
    (void)sprintf(p, "%s\n%22.15e %22.15e %22.15e %22.15e %22.15e %22.15e", p,
		m3GetZX(m6GetVP(m)), m3GetZY(m6GetVP(m)), m3GetZZ(m6GetVP(m)),
		m3GetZX(m6GetVV(m)), m3GetZY(m6GetVV(m)), m3GetZZ(m6GetVV(m)));

    return(p);
}
