/* file: $RCSfile: j2jd.c,v $
** rcsid: $Id: j2jd.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: j2jd.c,v $ - convert a scalar julian date into a jd date
** *******************************************************************
*/

#include "times.h"

JD
j2jd(double j)
{
    JD jd;

    jdSetDay(jd, j);
    jdSetHours(jd, 0.0);
    jdSetMinutes(jd, 0.0);
    jdSetSeconds(jd, 0.0);

    return(jd);
}
