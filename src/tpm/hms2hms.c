/* file: $RCSfile: hms2hms.c,v $
** rcsid: $Id: hms2hms.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: hms2hms.c,v $ - normalize an hms time
** *******************************************************************
*/

#include "times.h"

HMS
hms2hms(HMS hms)
{
    double x;

    /* convert to decimal hours */
    x = hms2h(hms);
    hmsSetHours(hms, floor(x));

    /* promote the minutes part */
    x = (x - floor(x)) * 60.0;
    hmsSetMinutes(hms, floor(x));

    /* promote the seconds part */
    x = (x - floor(x)) * 60.0;
    hmsSetSeconds(hms, x);

    return(hms);
}
