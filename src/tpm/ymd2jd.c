/* file: $RCSfile: ymd2jd.c,v $
** rcsid: $Id: ymd2jd.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: ymd2jd.c,v $ - convert a ymd time into a jd time
** *******************************************************************
*/

#include "times.h"

JD
ymd2jd(YMD ymd)
{
    JD jd;
    int m, y;

    y = ymdGetYear(ymd);
    m = ymdGetMonth(ymd);

    /* normalize the month */
    if (m < 1) {
	y -= (1 - m) / 12;
	m = (m % 12) + 12;
    }

    if (m > 12) {
	y += (m - 1) / 12;
	m = ((m - 1) % 12) + 1;
    }

    jdSetDay(jd, gcal2j(y, m, 0));
    jdIncDay(jd, ymdGetDay(ymd));

    /* now the fractional day...  */
    jd.hms = ymd.hms;

    /* julian days start 12 hours after civil days */
    jdDecHours(jd, 12.0);

    return(jd);
}
