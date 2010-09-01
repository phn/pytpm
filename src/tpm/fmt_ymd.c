/* file: $RCSfile: fmt_ymd.c,v $
** rcsid: $Id: fmt_ymd.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_ymd.c,v $ - format a ymd time
** *******************************************************************
*/

#include <stdio.h>
#include <string.h>
#include "times.h"

static char *dow[] = {
	"Sun",
	"Mon",
	"Tue",
	"Wed",
	"Thu",
	"Fri",
	"Sat",
};

static char *moy[] = {
	"Jan",
	"Feb",
	"Mar",
	"Apr",
	"May",
	"Jun",
	"Jul",
	"Aug",
	"Sep",
	"Oct",
	"Nov",
	"Dec",
};

#define NYMDBUF 5
static char ymdbuf[NYMDBUF][32];
static int nxtymdbuf = 0;

char *
fmt_ymd(YMD ymd)
{
    char *p;
    double j;	/* julian day number of target time */
    int fpart;
    int ipart;
    int today;

    /* get a buffer */
    p = ymdbuf[nxtymdbuf++];
    nxtymdbuf %= NYMDBUF;

    /* normalize the time */
    ymd = ymd2ymd(ymd);

    /* get the julian day number */
    j = ymd2j(ymd);

    /* get the day of the week */
    today = j2dow(j);

    ipart = (int)ymdGetSeconds(ymd);
    fpart = 1e3 * (ymdGetSeconds(ymd) - ipart);

    (void)sprintf(p, "%3.3s %3.3s %2d %02d:%02d:%02d.%03d %4d",
	    dow[today],
	    moy[ymdGetMonth(ymd)-1],
	    (int)ymdGetDay(ymd),
	    (int)ymdGetHours(ymd),
	    (int)ymdGetMinutes(ymd),
	    ipart, fpart,
	    ((ymdGetYear(ymd) > 0) ? ymdGetYear(ymd) : (1-ymdGetYear(ymd))));

    if (ymdGetYear(ymd) <= 0) {
	(void)strcat(p, " BC");
    }

    return(p);
}
