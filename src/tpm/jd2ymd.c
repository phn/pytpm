/* file: $RCSfile: jd2ymd.c,v $
** rcsid: $Id: jd2ymd.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: jd2ymd.c,v $ - convert a jd time into a ymd time
** *******************************************************************
*/

#include "times.h"

YMD
jd2ymd(JD jd)
{
    YMD ymd;
    double j;
    double x;
    int y, m, d;

    j = jdGetDay(jd);
    j2gcal(&y, &m, &d, j);
    ymdSetYear(ymd, y);
    ymdSetMonth(ymd, m);
    ymdSetDay(ymd, (double)d);

    x = (j - floor(j));
    /*
    ** we do this next step because the rounding of j in j2gcal()
    ** either credits or debits us with 12 hours
    */
    if (x < 0.5) {
	x += 0.5;
    } else {
	x -= 0.5;
    }
    ymdIncDay(ymd, x);

    /* pick up the hours, minutes, and seconds */
    ymd.hms = jd.hms;

    return(ymd);
}
