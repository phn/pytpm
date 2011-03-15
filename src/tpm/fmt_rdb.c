/* file: $RCSfile: fmt_rdb.c,v $
** rcsid: $Id: fmt_rdb.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_rdb.c,v $ - format an rdb date
** *******************************************************************
*/

#include <stdio.h>
#include "times.h"

#define NRDBBUF 5
static char rdbbuf[NRDBBUF][32];
static int nxtrdbbuf = 0;

char *
fmt_rdb(double rdb)
{
    char *p;
    int fpart;
    int ipart;

    /* get a buffer */
    p = rdbbuf[nxtrdbbuf++];
    nxtrdbbuf %= NRDBBUF;
    *p = '\0';

    /* make sure the time is well-formed */
    rdb = rdb2rdb(rdb);

    ipart = (int)rdb;
    fpart = 1e6 * (rdb - ipart);

    (void)sprintf(p, "%d.%06d", ipart, fpart);

    return(p);
}
