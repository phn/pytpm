/* file: $RCSfile: dms2d.c,v $
** rcsid: $Id: dms2d.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: dms2d.c,v $ - convert dms angle to scalar degrees
** *******************************************************************
*/

#include "times.h"

double
dms2d(DMS dms)
{
    double d;

    d = dmsGetDegrees(dms);
    d += dmsGetMinutes(dms) / 60.0;
    d += dmsGetSeconds(dms) / 3600.0;

    return(d);
}
