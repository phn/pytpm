/* file: $RCSfile: fmt_ymd_raw.c,v $
** rcsid: $Id: fmt_ymd_raw.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_ymd_raw.c,v $ - format a ymd time as it is expected from a user.
** *******************************************************************
*/

#include <stdio.h>
#include "times.h"

#define NYMDBUF 5
static char ymdbuf[NYMDBUF][32];
static int nxtymdbuf = 0;

char *
fmt_ymd_raw(YMD ymd)
{
    char *p;

    /* get a buffer */
    p = ymdbuf[nxtymdbuf++];
    nxtymdbuf %= NYMDBUF;

    (void)sprintf(p, "%d %d %.15g %.15g %.15g %.15g",
	    ymdGetYear(ymd),
	    ymdGetMonth(ymd),
	    ymdGetDay(ymd),
	    ymdGetHours(ymd),
	    ymdGetMinutes(ymd),
	    ymdGetSeconds(ymd));

    return(p);
}
