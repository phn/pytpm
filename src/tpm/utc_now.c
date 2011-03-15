/* file: $RCSfile: utc_now.c,v $
** rcsid: $Id: utc_now.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: utc_now.c,v $ - return the current UTC julian date, to the nearest second.
** *******************************************************************
*/

#include <time.h>
#include <stdio.h>
#include "times.h"

double
utc_now(void)
{
    double utc;
    time_t t;
    struct tm *ptm;

    /* get the system time in seconds */
    t = time(NULL);

    /* convert to UTC */
    ptm = gmtime(&t);

    /* get the julian date of the start of the day */
    utc = gcal2j(1900+ptm->tm_year, ptm->tm_mon+1, ptm->tm_mday) - 0.5;

    /* offset to now */
    utc += (ptm->tm_hour + (ptm->tm_min + (ptm->tm_sec / 60.0)) / 60.0) / 24.0;

    return(utc);
}
