/* file: $RCSfile: ymd2ymd.c,v $
** rcsid: $Id: ymd2ymd.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: ymd2ymd.c,v $ - normalize a ymd time
** *******************************************************************
*/

#include "times.h"

YMD
ymd2ymd(YMD ymd)
{
    double j;	/* julian day number */
    double x;
    int y, m, d;

    j = ymd2j(ymd);

    j2gcal(&y, &m, &d, j);
    ymdSetYear(ymd, y);
    ymdSetMonth(ymd, m);
    ymdSetDay(ymd, d);

    x = j - floor(j);
    /*
    ** we do this next step because the rounding of j in j2gcal()
    ** either credits or debits us with 12 hours
    */
    if (x < 0.5) {
	x += 0.5;
    } else {
	x -= 0.5;
    }

    /* promote the hours */
    x = (x - floor(x)) * 24.0;
    ymdSetHours(ymd, floor(x));

    /* promote the minutes */
    x = (x - floor(x)) * 60.0;
    ymdSetMinutes(ymd, floor(x));

    /* promote the seconds */
    x = (x - floor(x)) * 60.0;
    ymdSetSeconds(ymd, x);

    return(ymd);
}
